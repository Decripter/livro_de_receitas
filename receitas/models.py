from django.db import models




class Chef(models.Model):
    nome_chef = models.CharField('Nome', max_length=200, unique=True)

    def __str__(self):
        return self.nome_chef



class Receita(models.Model):
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    receita = models.TextField('Receita')

    def __str__(self):
        return self.choice_text