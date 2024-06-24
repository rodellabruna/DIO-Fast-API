from fastapi import FastAPI

from workout_api.contrib.models import BaseModel
from workout_api.contrib.repository.models import *


app = FastAPI(title="WorkoutApii")

# if __name__ == 'main':
#     import uvicorn
#     uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)
