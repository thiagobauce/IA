from django.db import models
from django.utils import timezone
from django import forms 

class Arquivo(models.Model):
    arquivo = models.FileField(upload_to='files/%Y/%m/')
    nome = models.CharField(max_length=50,default='NULL')
    email = models.CharField(max_length=50, default='meuprojeto7225@gmail.com')
    descricao = models.TextField(max_length=300, blank = True)
    
    def __str__(self):
        return self.nome

class FormArquivo(forms.ModelForm):
    class Meta:
        model = Arquivo
        exclude = ()    


"""extension = os.path.join('projeto new/media').splitext(nome_arq)
    if(extension in 'jpg' or extension in 'png'):
        tipo = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    elif(extension in 'mp4'):
        #chama recorte de frames
        pass"""