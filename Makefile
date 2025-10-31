SERVICE ?= autonomy-api
build:
	docker build -t $(SERVICE):local .
deploy:
	gcloud run deploy $(SERVICE) --source . --project $$GCP_PROJECT_ID --region $$GCP_REGION --allow-unauthenticated --quiet
smoke:
	./ops/smoke.sh $(SERVICE)
heal:
	./ops/autoheal.sh $(SERVICE) --one-shot
