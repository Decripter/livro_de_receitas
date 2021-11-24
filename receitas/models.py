from django.db import models

# Model dos chefs
class ChefModel(models.Model):
    nome_chef = models.CharField('Nome', max_length=200, unique=True)
    def __str__(self):
        return self.nome_chef # Retorna o nome do chef para visualização no painel administrativo

# Model das receitas
class ReceitaModel(models.Model):
    chef = models.ForeignKey(ChefModel, on_delete=models.CASCADE) # Quando o chef for removido todas as receitas dele também serão removidas
    receita = models.TextField('Receita') # Atribui um apelido que será exibido no painel administrativo
    def __str__(self):
        return "Chef: " + str(self.chef) +" - "+ str(self.receita[0:15])+" ..." # Customiza a exibição das receitas no painel administrativo
        