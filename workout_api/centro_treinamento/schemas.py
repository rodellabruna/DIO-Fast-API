from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated(str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20))
    endereço: Annotated(str, Field(description='Endereco do centro de treinamento', example='Rua X Quadra 2, São Paulo', max_length=60))
    proprietarop: Annotated(str, Field(description='Proprietario do centro de treinamento', example='Marcos', max_length=30))
