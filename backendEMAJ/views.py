from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from backendEMAJ.models import User
from backendEMAJ import models


# Create your views here.
@require_GET
def user(request):
    #a = User(request.name, request.price)
    #user= a.objects.all()
    #print(a.objects.all())
    return HttpResponse("Sucesso.")

@require_POST
def createAssistido(request):
    print(request)

    #models.Assistido(request.nome, request.rg).save()
    
    return HttpResponse("Sucesso")