import json
from pydantic import BaseModel, field_validator
import re

class ModelUsuario(BaseModel):
    name : str
    email : str
    usuario : str
    senha : str
    role : str
    imagem : str
    
################# Validações #################

    @field_validator('email')
    @classmethod
    def email_must_be_email(cls, email):
        assert "@furg.br" in email
        return email
