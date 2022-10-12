from django.shortcuts import render
from .models import FormArquivo
from django.contrib import messages
from pymongo import MongoClient

client = pymongo.MongoClient('connection_string')
db = client['db_name']


# Create your views here.
def index(request):
    if request.method != 'POST':
        form=FormArquivo()
        return render(request,'upfile/index.html',{'form' : form})
    
    form = FormArquivo(request.POST, request.FILES)
    form.save()
    messages.success(request,'Arquivo Enviado com Sucesso')    
    return render(request,'upfile/index.html',{'form' : form})