import json
from pydantic import BaseModel, field_validator
import re

class ModelDemanda(BaseModel):
    titulo: str
    usuario: str
    descricao: str
    image: str or None
    