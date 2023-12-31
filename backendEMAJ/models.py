from djongo import models
from django import forms


class Processo(models.Model):
    numeroProcesso = models.BigIntegerField()
    representante = models.CharField(max_length=100)
    escritorio = models.CharField(max_length=100)
    observacao = models.TextField()


class Demanda(models.Model):
    escritorio = models.CharField(max_length=100)
    assunto = models.TextField()
    processo = models.ArrayReferenceField(to=Processo)
    data = models.DateField()
    
    
class Atendimento(models.Model):
    data = models.DateField()
    
    #? 
    #responsaveis = models.ArrayReferenceField(to=Usuario)
    
    resumo = models.TextField()
    processo = models.ArrayReferenceField(to=Processo)
    tipo = models.CharField(max_length=100)
    forma = models.CharField(max_length=100)
    providencia = models.CharField(max_length=100)
    

class Documento(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    observacao = models.TextField()
    url = models.URLField()
    

    
class Pecas(models.Model):
    name = models.CharField(max_length=100)
    observacao = models.TextField()
    url = models.URLField()
    
class Representado(models.Model):
    id_uuid = models.CharField(max_length=100, unique=True, primary_key=True)
    name = models.CharField(max_length=100, null=True)
    cpf = models.CharField(max_length=11, null=True)
    rg = models.IntegerField(20, null=True)
    dataNasc = models.DateField(max_length=8, null=True)
    estadoCivil = models.CharField(max_length=100, null=True)

    def returnAsDict(self):
        return self.__dict__
    

class Assistido(models.Model):
    id_uuid = models.CharField(max_length=100, unique=True, null=True)
    name = models.CharField(max_length=100, null=False)
    cpf = models.CharField(max_length=11, unique=True, null=False)
    rg = models.IntegerField(20, unique=True, null=False)
    dataNasc = models.DateField(max_length=8, null=False)
    email = models.EmailField(null=False)
    estadoCivil = models.CharField(max_length=100)
    telefone1 = models.IntegerField(null=False)
    telefone2 = models.IntegerField(null=False)
    profissao = models.CharField(max_length= 20)
    renda = models.FloatField(null=False)
    dependentes = models.CharField(max_length=100)
    representado = models.ForeignKey(Representado, null=True, on_delete=models.CASCADE)
    endereco = models.TextField(max_length= 50, null=False)
    #processos = models.ArrayReferenceField(to=Processo)
    conhecido = models.CharField(max_length=100)
    demandas = models.ArrayReferenceField(to=Demanda)
    atendimento = models.ArrayReferenceField(to=Atendimento)
    documentos = models.ArrayReferenceField(to=Documento)
    pecas = models.ArrayReferenceField(to=Pecas)
    
    def to_json(self):
        return {
            "id_uuid": self.id_uuid,
            "name": self.name,
            "cpf": self.cpf,
            "rg": self.rg,
            "dataNasc": self.dataNasc,
            "email": self.email,
            "estadoCivil": self.estadoCivil,
            "telefone1": self.telefone1,
            "telefone2": self.telefone2,
            "profissao": self.profissao,
            "renda": self.renda,
            "dependentes": self.dependentes,
            "representado": self.representado_id,
            "endereco": self.endereco,
            "conhecido": self.conhecido,
        }

    def returnAsDict(self):
        return self.__dict__
    

class Usuario(models.Model):
    id_uuid = models.CharField(max_length=100, unique=True, null=True)
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)
    role = models.CharField(max_length=100, null=False)
    image = models.CharField(max_length=100, null=True)
    processos = models.ArrayReferenceField(to=Processo)

    def to_json(self):
        return {
            "id_uuid": self.id_uuid,
            "name": self.name,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "role": self.role,
            "image": self.image
        }

    


# Create your models here.
