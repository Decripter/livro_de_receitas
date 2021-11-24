from rest_framework.test import APITestCase
from django.test import Client
from receitas.models import ChefModel
from rest_framework import status
from django.http import HttpResponse
import requests

client = Client()

# Testes do módulo Chef
class TestChefModel(APITestCase):

    # Configurando o teste, criando os chefs 1 e 2: 
    def setUp(self):
        self.chef_1 = ChefModel.objects.create(nome_chef = 'Marcos')
        self.chef_2 = ChefModel.objects.create(nome_chef = 'Juliana')

    # Testando listar receitas no modulo Chef:
    
        # Testa se a resposta é uma lista vazia:
    def test_ver_receitas_recebendo_resposta_vazia(self):
        response = client.get('/chef/')
        self.assertEqual(response.content,  b'[]')
    
        # Testa se a resposta não é uma lista vazia:
    def test_ver_receitas_recebendo_resposta_vazia(self):
        response = client.post('/chef/', {'chef': 1, 'receita': 'cafe com leite'})
        response = client.get('/chef/')
        self.assertNotEqual(response.content,  b'[]')


    # Testando criação de receitas:
    
        # Testa a criação de uma receita com o chef_1(Marcos)
    def test_criar_receita_com_chef_1(self):
        response = client.post('/chef/', {'chef': 1, 'receita': 'cafe com leite'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Testa a criação de uma receita com o chef_2(Juliana)
    def test_criar_receita_com_chef_2(self):
        response = client.post('/chef/', {'chef': 2, 'receita': 'cafe com leite'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Testa se é possível criar receita com um chef inexistente
    def test_criar_receita_com_chef_inexistente(self):
        response = client.post('/chef/', {'chef': 101, 'receita': 'cafe com leite'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Testa se é possível criar uma receita sem informar o chef
    def test_criar_receita_sem_informar_chef(self):
        response = client.post('/chef/', {'receita': 'cafe com leite'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Testa se é possível criar uma receita vazia
    def test_criar_receita_vazia(self):
        response = client.post('/chef/', {'chef': 1, 'receita': ''})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Testa se é possível criar uma receita sem informar a receita
    def test_criar_receita_vazia(self):
        response = client.post('/chef/', {'chef': 1})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    # Testando alteração de receitas:

    def test_alterando_receitas(self):
        
        # Criando uma receita
        response = client.post('/chef/', {'chef': 1, 'receita': 'cafe com leite'})
        response = client.get('/chef/')
        response = requests.delete('http://localhost:8000/chef/1')
        print(response.status_code)

       


    # def test_deletando_receita(self):
    #     # Criando uma receita
    #     response = client.post('/chef/', {'chef': 1, 'receita': 'cafe com leite'})

    #     response = client.delete('/chef/1', {"id": 1} )

    #     print(response.status_code)
    #     response = client.get('/chef/')
    #     self.assertEqual(response.content,  b'[]')

