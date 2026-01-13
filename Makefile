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
	docker rm -f open-webui
	docker compose up -d open-webui

open-webui-update:: create-data-dirs
	docker rm -f open-webui
	docker compose pull open-webui

searxng-restart:: create-data-dirs
	docker rm -f searxng
	docker compose up -d searxng

searxng-update:: create-data-dirs
	docker rm -f searxng
	docker compose pull searxng

tika-restart:: create-data-dirs
	docker rm -f tika
	docker compose up -d tika

tika-update:: create-data-dirs
	docker rm -f tika
	docker compose pull tika	

ollama-restart:: create-data-dirs
	docker rm -f ollama
	docker compose up -d ollama

ollama-update:: create-data-dirs
	docker rm -f ollama
	docker compose pull ollama

ollama-update-models::
	docker compose exec ollama sh -c 'ollama ls | tail -n +2 | cut -d" " -f1 | xargs --verbose -n 1 ollama pull'
	
user-model-metrics-webhook-restart:: create-data-dirs
	docker rm -f user-model-metrics-webhook
	docker compose up -d user-model-metrics-webhook

user-model-metrics-webhook-build::
	docker compose build user-model-metrics-webhook