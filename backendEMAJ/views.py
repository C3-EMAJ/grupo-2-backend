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

# Create your views here.
@require_POST
def user(request):
    requisicao = json.loads(request.body)
    newUser = Usuario(**requisicao)
    newUser.save()
    return HttpResponse("Sucesso.")

@require_POST
def deleteUser(request):
    requisicao = json.loads(request.body)
    id = requisicao.get('id', None)

    if id is not None:
        try:
            user = Usuario.objects.get(id=id)
            user.delete()
            return JsonResponse({"success": True, "message": "Usuario deletado com sucesso"})
        except Usuario.DoesNotExist:
            return JsonResponse({"success": False, "message": "Usuario não encontrado"})
    else:
        return JsonResponse({"success": False, "message": "Parâmetro 'id' ausente na requisição"})


@require_POST
def createAssistido(request):
    requisicao = json.loads(request.body)
    newAssistido = Assistido(**requisicao)
    newAssistido.save()
    # const data = {name, cpf, rg, date, isChecked,
    #  email, telefone1, telefone2, profissao, renda, dependentes}
    return JsonResponse({"success":True})

@require_POST
def deleteAssistido(request):
    requisicao = json.loads(request.body)
    id = requisicao.get('id', None)

    if id is not None:
        try:
            assistido = Assistido.objects.get(id=id)
            assistido.delete()
            return JsonResponse({"success": True, "message": "Assistido deletado com sucesso"})
        except Assistido.DoesNotExist:
            return JsonResponse({"success": False, "message": "Assistido não encontrado"})
    else:
        return JsonResponse({"success": False, "message": "Parâmetro 'id' ausente na requisição"})

#@require_POST
#def editAssistido(request):
#    requisicao = json.loads(request.body)
#    id = requisicao.get('id', None)
#   novo_name = requisicao.get('novo_name', None)
#
#    if id is not None and novo_name is not None:
#        try:
#            assistido = Assistido.objects.get(id=id)
#
 #           # Atualize os campos do Assistido com os novos valores do JSON da requisição
  #          for key, value in requisicao.items():
   #             if key != 'id' and key != 'novo_name':
    #                setattr(assistido, key, value)
#
 #           # Atualize o nome (caso tenha sido alterado)
  #          if current_name != new_name:
   #             assistido.name = new_name
#
 #           assistido.save()  # Salve as alterações no banco de dados
  #          return JsonResponse({"success": True, "message": "Assistido editado com sucesso"})
   #     except Assistido.DoesNotExist:
    #        return JsonResponse({"success": False, "message": "Assistido não encontrado"})
    #else:
      #  return JsonResponse({"success": False, "message": "Parâmetros ausentes na requisição"})