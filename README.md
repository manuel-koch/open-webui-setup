# Open WebUI Setup

A docker-compose configuration that runs

- [Open WebUI - Docs](https://docs.openwebui.com/), [Open WebUI - Github](https://github.com/open-webui/open-webui)
- [SearXNG - Docs](https://docs.searxng.org/), [SearXNG - Github](https://github.com/searxng/searxng)
- [Tika - Docs](https://tika.apache.org/), [Tika - Github](https://github.com/apache/tika)

The docker compose configuration requires the following environment variables to be set:

- OPEN_WEBUI_PORT
- OPEN_WEBUI_BASE_URL
- OPEN_WEBUI_SECRET_KEY
- SEARCHXNG_PORT
- SEARXNG_BASE_URL
- SEARXNG_SECRET
- TIKA_PORT

## Open WebUI Hints

### Entering multiline text or markdown formatted content broken

Disable the option "Rich-Text-Input for Chats" in your personal settings under "Interface".

# Use models via Open WebUI

# macai

Native MacOS app to chat with LLMs: [macai](https://github.com/Renset/macai)

Use the following settings to chat with models provided by __Open WebUI__:

- API Type: OpenAI
- API URL: `<OPEN_WEB_UI_BASE_URL>/api/chat/completions`, e.g. OPEN_WEB_UI_BASE_URL=http://localhost:20080
- API Key: The API Key you have configured in __Open WebUI__ for your user
- Click the "Update" button to load available models
- Choose a model provided by __Open WebUI__
- Click "Test API token & model" to verify connection