restart:
	docker compose down
	docker rmi exam_bot-bot:latest
	docker compose up

stop:
	docker compose down
	docker rmi exam_bot-bot:latest