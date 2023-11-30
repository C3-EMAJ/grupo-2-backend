import json
from pydantic import BaseModel, field_validator
import re

class ModelUsuario(BaseModel):
    name : str
    email : str
    username : str
    password : str
    role : str
    image : str
    
################# Validações #################

    @field_validator('email')
    @classmethod
    def email_must_be_email(cls, email):
        assert "@furg.br" in email
        return (f"Email {email} não é do dominio furg. '@furg.br'.")
