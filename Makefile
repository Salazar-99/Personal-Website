#Add a testing rule
 
development
	docker-compose -f docker-compose.dev.yml up

deploy
	make build
	make production

build
	docker-compose -f docker-compose.production.yml build

production
	docker-compose -f docker-compose.production.yml up