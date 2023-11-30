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
        #if e.errors().
        return JsonResponse(data={
            "error":str(e.errors()),
            "message": str("Ocorreu um erro inesperado."),
            "statuscode": 400
        }, status=400)
    
    ##### Criando o UUID #####

    newUUID = uuid.uuid4()
    newUsuario = Usuario(**requisicao)
    setattr(newUsuario, "id_uuid", newUUID)
    newUsuario.save()

    return JsonResponse(data={"success": True, "message": "Usuário criado com sucesso."}, status=201)

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
    
    representado = requisicao.get('representado', None)
    newUUIDrep = uuid.uuid4()
    del requisicao['representado']
    
    if representado != None:
        print(representado)
        newRepresentado = Representado(**representado)
        setattr(newRepresentado, "id_uuid", newUUIDrep)
        newRepresentado.save()
    
    ##### Criando o UUID #####
    
    newAssistido = Assistido(**requisicao)
    newUUIDas = uuid.uuid4()
    setattr(newAssistido, "id_uuid", newUUIDas)
    setattr(newAssistido, "representado", newRepresentado)
    newAssistido.save()

    return JsonResponse(data={"success": True, "message": "Assistido criado com sucesso"}, status=201)

@require_POST
def deleteAssistido(request):
    requisicao = json.loads(request.body)
    id_uuid = requisicao.get('id_uuid', None)


    if id_uuid is not None:
        try:
            assistidoDeletado=Assistido.objects.get(id_uuid=id_uuid)
            print(assistidoDeletado)
            representados_id = assistidoDeletado.representado_id
            print(representados_id)
            assistidoDeletado.delete()
            Representado.objects.get(id_uuid=representados_id).delete()

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
    

############ ROTAS DE GET ###################

@require_GET
def getUsers(request):
    try:
        users = Usuario.objects.all()
        if len(users) < 1:
            return JsonResponse(data={"success": False, "message": "Nenhum usuario encontrado."}, status=404)    
        # Converte a lista de usuários em um array de objetos JSON
        users_json = [user.to_json() for user in users]

        return JsonResponse(users_json, safe=False, status=200)
    except Usuario.DoesNotExist:
        return JsonResponse(data={"success": False, "message": "Nenhum usuario encontrado."}, status=404)
    
@require_GET
def getUserByName(request):
    nome=request.GET.get('name')
    try:
        
        user = Usuario.objects.get(name=nome)
        if user == None:
            return JsonResponse(data={"success": False, "message": "Nenhum usuario encontrado."}, status=404)    
        # Converte a lista de usuários em um array de objetos JSON
        user_json = user.to_json()

        return JsonResponse(user_json, safe=False, status=200)
    except Usuario.DoesNotExist:
        return JsonResponse(data={"success": False, "message": "Nenhum usuario encontrado."}, status=404)

@require_GET
def getAssistidos(request):
    try:
        assistidos = Assistido.objects.all()
        if len(assistidos) < 1:
            return JsonResponse(data={"success": False, "message": "Nenhum assistido encontrado."}, status=404)    
        # Converte a lista de usuários em um array de objetos JSON
        assistidos_json = [assistido.to_json() for assistido in assistidos]

        return JsonResponse(assistidos_json, safe=False, status=200)
    except Assistido.DoesNotExist:
        return JsonResponse(data={"success": False, "message": "Nenhum assistido encontrado."}, status=404)

################# TESTES #################

@require_POST
def login(request):
    requisicao = json.loads(request.body)
    email = requisicao.get('email', None)
    password = requisicao.get('password', None)
    try:
        users = Usuario.objects.get(email=email)
        if users.password == password: #################### É AQUI NESSE JSON RESPONSE STATUS=200 que voces vão por o token.
            ##### Assistam o video q mandei no discord no chat WORK
            return JsonResponse(data={"name": users.name, "username": users.username, "role": users.role, "image": users.image}, safe=False, status=200)
        else:
            return JsonResponse(data={"success": False, "message": "Senha errada."}, status=404)

    except Usuario.DoesNotExist:
        return JsonResponse(data={"success": False, "message": "Nenhum usuario encontrado com este email."}, status=404)

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