start::
	docker compose up -d

shutdown::
	docker compose down

open-webui-restart::
	docker compose stop open-webui
	docker compose start open-webui

open-webui-update::
	docker compose pull open-webui

searxng-restart::
	docker compose stop searxng
	docker compose start searxng

searxng-update::
	docker compose pull searxng

tika-restart::
	docker compose stop tika
	docker compose start tika

tika-update::
	docker compose pull tika	