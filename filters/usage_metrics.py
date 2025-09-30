"""
title: Usage Metrics
author: Manuel Koch
author_url: https://github.com/manuel-koch/open-webui-setup
funding_url: https://github.com/manuel-koch/open-webui-setup
version: 1.0
"""

import logging
from pydantic import BaseModel, Field
from typing import Optional
from pathlib import Path
from datetime import datetime, timezone
import json

logger = logging.getLogger(__name__)


class Filter:
    class Valves(BaseModel):
        priority: int = Field(
            default=0, description="Priority level for the filter operations."
        )

    class UserValves(BaseModel):
        pass

    def __init__(self):
        # Indicates custom file handling logic. This flag helps disengage default routines in favor of custom
        # implementations, informing the WebUI to defer file-related operations to designated methods within this class.
        # Alternatively, you can remove the files directly from the body in from the inlet hook
        # self.file_handler = True

        # Initialize 'valves' with specific configurations. Using 'Valves' instance helps encapsulate settings,
        # which ensures settings are managed cohesively and not confused with operational flags like 'file_handler'.
        self.valves = self.Valves()
        pass

    async def inlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        # Modify the request body or validate it before processing by the chat completion API.
        # This function is the pre-processor for the API where various checks on the input can be performed.
        # It can also modify the request before sending it to the API.

        # print(f"inlet:{__name__} 8")
        # print(f"inlet:body:{body}")
        # print(f"inlet:user:{__user__}")

        return body

    async def outlet(
        self, body: dict, __event_emitter__, __user__: Optional[dict] = None
    ) -> dict:
        # Modify or analyze the response body after processing by the API.
        # This function is the post-processor for the API, which can be used to modify the response
        # or perform additional checks and analytics.

        # print(f"outlet:{__name__}")
        # print(f"outlet:body:{body}")

        try:
            timestamp = datetime.now(tz=timezone.utc)
            user_id = __user__["id"]
            messages = body.get("messages", [])
            last_message_with_usage = next(
                (m for m in reversed(messages) if m.get("usage", {})), None
            )
            usage = last_message_with_usage["usage"] if last_message_with_usage else {}
            metric_data = {
                "timestamp": timestamp.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "model": body.get("model", ""),
                "user_id": user_id,
                "user_name": __user__.get("name", ""),
                "user_email": __user__.get("email", ""),
                "usage": usage,
            }
            path = (
                Path("data")
                / "usage_metrics"
                / f"{timestamp.strftime('%Y-%m')}"
                / user_id
                / f"{int(timestamp.timestamp()*1000)}.json"
            ).absolute()
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(metric_data, indent=2))
            logger.info(f"Saved usage metric to {path}")
        except:
            logger.exception("Failed to save usage metrics")
            await __event_emitter__(
                {
                    "type": "notification",
                    "data": {
                        "type": "error",
                        "content": f"Failed to save usage metrics: {str(e)}",
                    },
                }
            )
        return body
