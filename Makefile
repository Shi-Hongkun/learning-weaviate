migrate:
	@alembic upgrade head

test:
	@alembic upgrade head
	@clear
	@pytest  --durations=0 -v --cov=app

format:
	@isort app/
	@isort tests/
	@black app/
	@black tests/