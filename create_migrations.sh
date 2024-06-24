PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m "Initial migration"
PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head
