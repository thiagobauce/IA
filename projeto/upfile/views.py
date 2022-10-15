from django.shortcuts import render
from django.contrib import messages
from pymongo import MongoClient
from .models import User, Arquivo,FormUpload
import os, gridfs, fileinput

client = MongoClient(
    'mongodb+srv://iadmin:iadmin@iacluster.plyafn9.mongodb.net/?retryWrites=true&w=majority')

#Define Db Name
dbname = client['upfile']
fs = gridfs.GridFS(dbname)

#Define Collection
collection1 = dbname['users']
collection2 = dbname['arquivos']

def index(request):
    #users = User.objects.all() selec * from USER
    return render(request, 'upfile/index.html')

def insert(request):  
    if request.method != 'POST':
        form = FormUpload()
        return render(request, 'upfile/insere.html',{'form' : form})
    
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    sexo = request.POST.get('sexo')
    cidade = request.POST.get('cidade')
    estado = request.POST.get('estado')
    descricao = request.POST.get('descricao')
     
    arquivo = request.POST.get('arquivo')
    
    
    if not nome:
        messages.error(request,'Campo *nome* é obrigatório')
    elif not sobrenome:
        messages.error(request,'Campo *sobrenome* é obrigatório')
    elif not sexo:
        messages.error(request,'Campo *sexo* é obrigatório')
    elif not email:
        messages.error(request,'Campo *email* é obrigatório')
    elif not cidade:
        messages.error(request,'Campo *cidade* é obrigatório')
    elif not estado:
        messages.error(request,'Campo *estado* é obrigatório')
    elif not descricao:
        messages.error(request,'Campo *descricao* é obrigatório')
    elif not arquivo:
        messages.error(request,'Campo *arquivo* é obrigatório')    
    else:
        user={
            'nome':nome,
            'sobrenome':sobrenome,
            'sexo':sexo,
            'email':email,
            'cidade':cidade,
            'estado':estado,
            'descricao':descricao
            }
        collection1.insert_one(user)

        form = FormUpload(request.FILES)
        if form.is_valid():
            form.save()
        
        split_tup = os.path.splitext(arquivo)
        nomearq = split_tup[0]
        extensao = split_tup[1]
        
        
        
        #idarq = fs.put(arquivo,filename=nomearq,bar=extensao)
    
        arq = {
            'nomearq':nomearq,
            'extensao':extensao,
            'arquivo':arquivo,
            #'idarq':idarq
            }
        
        collection2.insert_one(arq)
        
        messages.success(request, ' Registro salvo com Sucesos')
    
    return render(request, 'upfile/insere.html',{'form' : form})


def tutorial(request):
    #users = User.objects.all() selec * from USER
    return render(request, 'upfile/tutorial.html')

def info(request):
    #users = User.objects.all() selec * from USER
    return render(request, 'upfile/info.html')