start:
	docker compose up

restart:
	docker compose down
	docker rmi kworkbot-latest
	docker compose up

stop:
	docker compose down