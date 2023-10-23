from django.shortcuts import render
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
def createAssistido(request):
    requisicao = json.loads(request.body)
    newAssistido = Assistido(**requisicao)
    newAssistido.save()
    # const data = {name, cpf, rg, date, isChecked,
    #  email, telefone1, telefone2, profissao, renda, dependentes}
    return JsonResponse({"success":True})