from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
#from backendEMAJ.models import User
from backendEMAJ import models
from backendEMAJ.models import Assistido
from backendEMAJ.models import Usuario
from backendEMAJ.services.validAssistido import ModelAssistido
from backendEMAJ.services.validUsuario import ModelUsuario
from pydantic import ValidationError
import uuid

# Create your views here.

################# Views do USUARIO #################
@require_POST
def createUser(request):
    requisicao = json.loads(request.body)
    try:
        validation = ModelUsuario(**requisicao)
    except ValidationError as e:
        return JsonResponse({
            "error":e.errors(),
            "statuscode": 400
        })
    
    #newUUID = uuid.uuid4           Futuramente implementar caso nao seja possivel usar o _id.
    #print(newUUID)
    
    newUsuario = Usuario(**requisicao)
    
    #setattr(newUsuario, "UUID", newUUID)       Teria que criar na model, e depois dele

    newUsuario.save()
    return JsonResponse({"success":True})

@require_POST
def deleteUser(request):
    requisicao = json.loads(request.body)
    email = requisicao.get('email', None)

    if email is not None: #                 Utilizando o email, pois é único, e também por que nao consegui utilizar o _id
        try:
            user = Usuario.objects.get(email = email)
            user.delete()
            return JsonResponse({"success": True, "message": "Usuario deletado com sucesso"})
        except Usuario.DoesNotExist:
            return JsonResponse({"success": False, "message": "Usuario não encontrado"})
    else:
        return JsonResponse({"success": False, "message": "Parâmetro 'id' ausente na requisição"})
    

@require_POST
def editUser(request):
    requisicao = json.loads(request.body)
    email = requisicao.get('email', None)
    print(email)
    if email is not None:
        try:
            user = Usuario.objects.get(email=email)

            # Atualize os campos do Assistido com os novos valores do JSON da requisição
            for key, value in requisicao.items():
                if key != 'email': #                Ainda não é possivel alterar o email.
                    setattr(user, key, value)

            user.save()  # Salve as alterações no banco de dados
            return JsonResponse({"success": True, "message": "Usuario editado com sucesso"})
        except Usuario.DoesNotExist:
            return JsonResponse({"success": False, "message": "Usuario não encontrado"})
    else:
        return JsonResponse({"success": False, "message": "Parâmetros ausentes na requisição"})



################# Views do ASSISTIDO #################

@require_POST
def createAssistido(request):
    requisicao = json.loads(request.body)
    try:
        validation = ModelAssistido(**requisicao)
    except ValidationError as e:
        return JsonResponse({
            "error":e.errors(),
            "statuscode": 400
        })

    newAssistido = Assistido(**requisicao)
    newAssistido.save()
    return JsonResponse({"success":True})

@require_POST
def deleteAssistido(request):
    requisicao = json.loads(request.body)
    cpf = requisicao.get('cpf', None)

    if cpf is not None:
        try:
            Assistido.objects.filter(cpf=cpf).delete()
            return JsonResponse({"success": True, "message": "Assistido deletado com sucesso"})
        except Assistido.DoesNotExist:
            return JsonResponse({"success": False, "message": "Assistido não encontrado"})
    else:
        return JsonResponse({"success": False, "message": "Parâmetro 'id' ausente na requisição"})


@require_POST
def editAssistido(request):
    requisicao = json.loads(request.body)
    cpf = requisicao.get('cpf', None)

    if cpf is not None:
        try:
            assistido = Assistido.objects.get(cpf=cpf)

            # Atualize os campos do Assistido com os novos valores do JSON da requisição
            for key, value in requisicao.items():
                print(key, value)
                if key != 'cpf':
                    setattr(assistido, key, value) # Database error

            assistido._do_update(forced_update=True)  # Salve as alterações no banco de dados
            return JsonResponse({"success": True, "message": "Assistido editado com sucesso"})
        except Assistido.DoesNotExist:
            return JsonResponse({"success": False, "message": "Assistido não encontrado"})
    else:
        return JsonResponse({"success": False, "message": "Parâmetros ausentes na requisição"})
    

################# TESTES #################

# def login(request):
#     requisicao = json.loads(request.body)
#     email = requisicao.get('email', None)
#     password = requisicao.get('password', None)

#     if email is not None:
#         try:
#             user = Usuario.objects.get(email=email)
#             if user.password == password:
#                 return True
#             return JsonResponse({"success": False, "message": "Senha incorreta."})
#         except Usuario.DoesNotExist:
#             return JsonResponse({"success": False, "message": "Usuario não encontrado"})
#     else:
#         return JsonResponse({"success": False, "message": "Email não encontrado."})