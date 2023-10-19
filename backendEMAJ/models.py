from djongo import models


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
    nome = models.CharField(max_length=100)
    observacao = models.TextField()
    url = models.URLField()
    

class Assistido(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.IntegerField(20)
    cpf = models.IntegerField()
    dataNasc = models.DateField(max_length=8)
    idade = models.IntegerField(max_length= 3)
    representante = models.CharField(max_length=100)
    renda = models.FloatField()
    endereco = models.TextField(max_length= 50)
    telefone1 = models.IntegerField(max_length= 15)
    telefone2 = models.IntegerField(max_length= 15)
    email = models.EmailField()
    #processos = models.ArrayReferenceField(to=Processo)
    conhecido = models.CharField(max_length=100)
    profissao = models.CharField(max_length= 20)
    dependentes = models.CharField(max_length=100)
    demandas = models.ArrayReferenceField(to=Demanda)
    atendimento = models.ArrayReferenceField(to=Atendimento)
    documentos = models.ArrayReferenceField(to=Documento)
    pecas = models.ArrayReferenceField(to=Pecas)
    

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    imagem = models.URLField()
    processos = models.ArrayReferenceField(to=Processo)

    


# Create your models here.
