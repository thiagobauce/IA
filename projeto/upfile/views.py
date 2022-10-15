from django.shortcuts import render, redirect
from django.contrib import messages
from pymongo import MongoClient
from .models import User, Arquivo, FormUpload, FormUser
import os, gridfs
from datetime import datetime


def encontra_pasta():
    ano = datetime.now().year
    mes = datetime.now().month
    dia = datetime.now().day
    
    return '/'+str(ano)+'/'+str(mes)+'/'+str(dia)

def salva_arquivo():
    parcial = encontra_pasta()
                
    caminho = 'C:/Users/ThiagoBauce/Documents/GitHub/IA/projeto/media/fotos' + parcial
    os.chdir(caminho) 
        
    for file in os.listdir():
        file_path = f"{caminho}/{file}" 
        with open(file_path, 'rb') as f: 
            idarq = fs.put(f)
            print(f)
            arquivo = os.path.split(f)
            nomearq = arquivo[0]
            extensao = arquivo[1]
            
            arq = {
                'nomearq':nomearq,
                'extensao':extensao,
                'arquivo':f,
                'idarq':idarq
            }
            if not collection2.find_one(arq):
                collection2.insert_one(arq)


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
        form1 = FormUpload()
        return render(request, 'upfile/insere.html',{'form1' : form1})
    
    form1 = FormUpload(request.POST,request.FILES)
    
    if form1.is_valid():
        form1.save()
        salva_arquivo()
        
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

        messages.success(request, ' Registro salvo com Sucesos')
    
    return redirect('index')

def tutorial(request):
    #users = User.objects.all() selec * from USER
    return render(request, 'upfile/tutorial.html')

def info(request):
    #users = User.objects.all() selec * from USER
    return render(request, 'upfile/info.html')