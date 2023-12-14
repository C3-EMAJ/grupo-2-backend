import json
from pydantic import BaseModel, field_validator
import re

class ModelDemanda(BaseModel):
    titulo: str
    assistido: str
    usuario: str
    descricao: str
    image: str
    