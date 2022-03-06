dev:
	docker build -f Dockerfile.dev -t personal-site-dev:latest .
	docker-compose -f docker-compose.dev.yml up

test:
	pytest

build:
	docker build -f Dockerfile -t personal-site-prod:latest .
