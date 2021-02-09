development:
	docker build -f Dockerfile.dev -t personal-site-dev:latest .
	docker-compose -f docker-compose.dev.yml up

test:
	pytest

deploy:
	make build
	make production

build:
	docker build -f Dockerfile -t personal-site:latest .
	docker build -f nginx/Dockerfile -t personal-site-nginx:latest .

production:
	docker-compose -f docker-compose.production.yml up