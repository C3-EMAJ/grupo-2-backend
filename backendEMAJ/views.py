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
from backendEMAJ.models import Representado
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
        return JsonResponse(data={
            "error":str(e.errors()),
            "statuscode": 400
        }, status=400)
    
    ##### Criando o UUID #####

    newUUID = uuid.uuid4()
    newUsuario = Usuario(**requisicao)
    setattr(newUsuario, "id_uuid", newUUID)
    newUsuario.save()

    return JsonResponse({"success":True})

@require_POST
def deleteUser(request):
    requisicao = json.loads(request.body)
    id_uuid = requisicao.get('id_uuid', None)

    if id_uuid is not None:
        try:
            user = Usuario.objects.get(id_uuid = id_uuid)
            user.delete()
            return JsonResponse(data={"success": True, "message": "Usuario deletado com sucesso"}, status=200)
        except Usuario.DoesNotExist:
            return JsonResponse(data={"success": False, "message": "Usuario não encontrado."}, status=404)
    else:
        return JsonResponse(data={"success": False, "message": "Parâmetro 'id_uuid' ausente na requisição."}, status=404)
    

@require_POST
def editUser(request):
    requisicao = json.loads(request.body)
    id_uuid = requisicao.get('id_uuid', None)
    print(id_uuid)
    if id_uuid is not None:
        try:
            user = Usuario.objects.get(id_uuid=id_uuid)

            # Atualize os campos do Assistido com os novos valores do JSON da requisição
            for key, value in requisicao.items():
                if key != 'id_uuid': 
                    setattr(user, key, value)

            user.save()  # Salve as alterações no banco de dados
            return JsonResponse(data={"success": True, "message": "Usuario editado com sucesso"}, status=200)
        except Usuario.DoesNotExist:
            return JsonResponse(data={"success": False, "message": "Usuario não encontrado."}, status=404)
    else:
        return JsonResponse(data={"success": False, "message": "Parâmetro 'id_uuid' não encontrado."}, status=404)



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
    
    # representado = requisicao.get('representado', None)
    # newUUID2 = uuid.uuid4()
    # del requisicao['representado']
    # newAssistido2= Assistido.objects.get(id_uuid=newUUID2)

    # if representado != None:
    #     print(representado)
    #     newRepresentado = Representado(**representado)
    #     setattr(newRepresentado, "id_uuid", newUUID)
    #     newRepresentado.save()
    #     newAssistido2.representado.add(newRepresentado)
    
    ##### Criando o UUID #####
    
    newAssistido = Assistido(**requisicao)
    newUUID = uuid.uuid4()
    setattr(newAssistido, "id_uuid", newUUID)
    newAssistido.save()

    return JsonResponse(data={"success": True, "message": "Assistido criado com sucesso"}, status=201)

@require_POST
def deleteAssistido(request):
    requisicao = json.loads(request.body)
    id_uuid = requisicao.get('id_uuid', None)


    if id_uuid is not None:
        try:
            varAssistido = Assistido.objects.get(id_uuid=id_uuid)
            Representado.objects.filter(id__in=[r.id for r in varAssistido.representado.all()]).delete()
            varAssistido.delete()

            # .delete()
            
            return JsonResponse(data={"success": True, "message": "Assistido deletado com sucesso"}, status=200)
        except Assistido.DoesNotExist:
            return JsonResponse(data={"success": False, "message": "Assistido não encontrado"}, status=404)
    else:
        return JsonResponse(data={"success": False, "message": "Parâmetro 'id_uuid' ausente na requisição"}, status=404)


@require_POST
def editAssistido(request):
    requisicao = json.loads(request.body)
    id_uuid = requisicao.get('id_uuid', None)

    if id_uuid is not None:
        try:
            assistido = Assistido.objects.get(id_uuid=id_uuid)

            # Atualize os campos do Assistido com os novos valores do JSON da requisição
            for key, value in requisicao.items():
                print(key, value)
                if key != 'id_uuid':
                    setattr(assistido, key, value)
                    
            assistido.save()  # Salve as alterações no banco de dados
            return JsonResponse(data={"success": True, "message": "Assistido editado com sucesso."}, status=200)
        except Assistido.DoesNotExist:
            return JsonResponse(data={"success": False, "message": "Assistido não encontrado."}, status=404)
    else:
        return JsonResponse(data={"success": False, "message": "Parâmetro 'id_uuid' não encontrado na requisição."}, status=404)
    

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