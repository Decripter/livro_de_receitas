from django.db import models

class ChefModel(models.Model):
    nome_chef = models.CharField('Nome', max_length=200, unique=True)

    def __str__(self):
        return self.nome_chef



class ReceitaModel(models.Model):
    chef = models.ForeignKey(ChefModel, on_delete=models.CASCADE)
    receita = models.TextField('Receita')

    def __str__(self):
        return "Chef: " + str(self.chef) +" - "+ str(self.receita[0:15])+" ..." 
        