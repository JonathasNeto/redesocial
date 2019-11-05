from django.db import models
from django.contrib.auth.models import User

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    coment = models.TextField()

    def __str__(self):
        return self.usuario.name

class Curtidas(models.Model):
    emog = models.ImageField()
    pessoa = models.ForeignKey(User ,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.emog)

class Perfil(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE, related_name='Perfil')
    descricao = models.TextField()
    telefone = models.CharField(max_length=12)
    cidade = models.CharField(max_length=50)
    data_criado = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField()
    comentarios = models.ManyToManyField(Comentario,related_name='Comentario')
    curtidas = models.ManyToManyField(Curtidas,related_name='Curtidas')
    amigos = models.ManyToManyField(User,related_name='Amigos')
    email = models.EmailField()

    def __str__(self):
        return self.usuario.name