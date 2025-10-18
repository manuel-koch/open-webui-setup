data/%:
	mkdir -p $@

create-data-dirs:: data/searxng/cache data/ollama data/open-webui data/tika data/user-model-metrics-webhook

start:: create-data-dirs
	docker compose up -d

start-foreground:: create-data-dirs
	docker compose up

logs::
	docker compose logs -f --tail=500

shutdown::
	docker compose down

open-webui-restart:: create-data-dirs
	docker compose stop open-webui
	docker compose start open-webui

open-webui-update:: create-data-dirs
	docker compose stop open-webui
	docker compose pull open-webui
	
searxng-restart:: create-data-dirs
	docker compose stop searxng
	docker compose start searxng

searxng-update:: create-data-dirs
	docker compose stop searxng
	docker compose pull searxng

tika-restart:: create-data-dirs
	docker compose stop tika
	docker compose start tika

tika-update:: create-data-dirs
	docker compose stop tika
	docker compose pull tika	

user-model-metrics-webhook-restart:: create-data-dirs
	docker compose stop user-model-metrics-webhook
	docker compose start user-model-metrics-webhook

user-model-metrics-webhook-build::
	docker compose build user-model-metrics-webhook