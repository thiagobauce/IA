from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django import forms

class User(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, blank=True)
    email = models.EmailField()
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    descricao = models.TextField(max_length=400)
    
    def __str__(self):
        return self.nome

      
class Arquivo(models.Model):
    nome = models.CharField(max_length=50)
    extensao = models.CharField(max_length=5)
    arquivo = models.FileField(upload_to='fotos/%Y/%m/%d')
    idarq = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

class FormUpload(forms.ModelForm):
    class Meta:
        model = Arquivo
        exclude = ('idarq','nome','extensao',)
        