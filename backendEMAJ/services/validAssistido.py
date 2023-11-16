import json
from pydantic import BaseModel, field_validator, ValidationError

class ModelAssistido(BaseModel):
    name : str
    cpf : str
    rg : int
    dataNasc : str
    email : str
    estadoCivil : str
    telefone1 : int
    telefone2 : int
    profissao : str
    idade : int
    renda : int
    dependentes : str

################# Validações #################

# Nenhuma por enquanto...