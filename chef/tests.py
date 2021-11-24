from django.test import Client
from rest_framework import status
from rest_framework.test import APITestCase

from receitas.models import ChefModel

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

    
    # Detalhando receitas:

        # Testando detalhar receita não cadastrada
    def test_detalhar_receita_nao_cadastrada(self):
        response = client.get('/chef/1/')
        self.assertEqual(response.content, b'{"detail":"N\xc3\xa3o encontrado."}')
    
        # Testando detalhar receita cadastrada
    def test_detalhar_receita_nao_cadastrada(self):
        response = client.post('/chef/', {'chef': 1, 'receita': 'cafe com leite'})
        response = client.get('/chef/1/')
        self.assertEqual(response.content, b'{"id":1,"chef":1,"receita":"cafe com leite"}')


    # Testando alteração de receitas:

        # Testando alterar receita cadastrada
    def test_alterando_receitas_cadastrada(self): 
        # Criando uma receita
        response = client.post('/chef/', {'chef': 1, 'receita': 'cafe com leite'})
        # Alterando a receita
        response = self.client.put('/chef/1/', {"id":1, 'chef': 1, 'receita': 'cafe com leite e acucar'})
        self.assertNotEqual(b'{"id":1,"chef":1,"receita":"cafe com leite"}', response.content)
    
        # Testando alterar receita não cadastrada
    def test_alterando_receitas_nao_cadastrada(self): 
        # Criando uma receita
        response = client.post('/chef/', {'chef': 1, 'receita': 'cafe com leite'})
        original = client.get('/chef/1/')

        # Alterando a receita
        response = self.client.put('/chef/100/', {"id":1, 'chef': 1, 'receita': 'cafe com leite e acucar'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    

    # Testando apagar receitas  
        # Testando delatar receita 1
    def test_deletando_receita_1(self): 
        # Criando uma receita
        response = client.post('/chef/', {'chef': 1, 'receita': 'cafe com leite'})
        # Deletando a receita
        response = self.client.delete('/chef/1/')
        response = client.get('/chef/1/')
        self.assertEqual(response.content, b'{"detail":"N\xc3\xa3o encontrado."}')
        
        # Testando deletar receita não cadastrada
    def test_deletando_receita_nao_cadastrada(self): 
        response = self.client.delete('/chef/100/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Testando deletar uma receita no meio de três
    def test_deletando_receita_3(self): 
        # Criando receitas
        response = client.post('/chef/', {'chef': 1, 'receita': 'cafe com leite'})
        response = client.post('/chef/', {'chef': 1, 'receita': 'macarrao com queijo'})
        response = client.post('/chef/', {'chef': 1, 'receita': 'lasanha'})
        # Deletando a receita
        response = self.client.delete('/chef/1/')
        response = client.get('/chef/')
        self.assertEqual(response.content, b'[{"id":2,"chef":1,"receita":"macarrao com queijo"},{"id":3,"chef":1,"receita":"lasanha"}]')




