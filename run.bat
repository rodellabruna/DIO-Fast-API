uvicorn workout_api.main:app --reload
PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(d)
PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head