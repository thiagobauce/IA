from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50, blank=True)
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
    arquivo = models.FileField()

    def __str__(self):
        return self.nome
