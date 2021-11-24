from rest_framework.test import APITestCase
from django.test import Client
from receitas.models import ChefModel
from rest_framework import status



client = Client()

# Testes do módulo Client
class TestClientModel(APITestCase):

    # Configurando o teste
    def setUp(self):
        # Criando os chefs 1, 2, 3 e 4:
        self.chef_1 = ChefModel.objects.create(nome_chef = 'Marcos')
        self.chef_2 = ChefModel.objects.create(nome_chef = 'Juliana')
        self.chef_3 = ChefModel.objects.create(nome_chef = 'Antonio')
        self.chef_4 = ChefModel.objects.create(nome_chef = 'Sofia')
        
        # Adicionando alguns registros: 
        client.post('/chef/', {'chef': 1, 'receita': 'cafe com leite'}) # Marcos
        client.post('/chef/', {'chef': 1, 'receita': 'macarrao com queijo'}) # Marcos
        client.post('/chef/', {'chef': 1, 'receita': 'suco de laranja'}) # Marcos
        client.post('/chef/', {'chef': 2, 'receita': 'cafe com leite'}) # Juliana
        client.post('/chef/', {'chef': 2, 'receita': 'macarrao com queijo'}) # Juliana
        client.post('/chef/', {'chef': 2, 'receita': 'suco de laranja'}) # Juliana
        client.post('/chef/', {'chef': 4, 'receita': 'lasanha'}) # Sofia
        
    # Testando listar receitas no modulo Client:
 
        # Testa se recebe a lista de receitas cadastradas
    def test_ver_receitas_resposta_nao_vazia(self):
        response = client.get('/client/')
        self.assertNotEqual(response.content,  b'[]')


    # Testando filtrar receitar pelo chef:

        # Testa filtrar receitas pelo chef_1:
    def test_filtrar_por_chef_1(self):
        response = client.get('/client/?chef=1')
        self.assertEqual(response.content, b'[{"id":1,"chef":1,"receita":"cafe com leite"},{"id":2,"chef":1,"receita":"macarrao com queijo"},{"id":3,"chef":1,"receita":"suco de laranja"}]')

         # Testa filtrar receitas pelo chef_2:
    def test_filtrar_por_chef_2(self):
        response = client.get('/client/?chef=2')
        self.assertEqual(response.content, b'[{"id":4,"chef":2,"receita":"cafe com leite"},{"id":5,"chef":2,"receita":"macarrao com queijo"},{"id":6,"chef":2,"receita":"suco de laranja"}]')

         # Testa filtrar receitas pelo chef_3:
    def test_filtrar_por_chef_3(self):
        response = client.get('/client/?chef=3')
        self.assertEqual(response.content, b'[]')

        # Testa filtrar receitas pelo chef_4:
    def test_filtrar_por_chef_4(self):
        response = client.get('/client/?chef=4')
        self.assertEqual(response.content, b'[{"id":7,"chef":4,"receita":"lasanha"}]')
    

    # Testando buscar por texto da receita:

        # Testa buscar receitas por cafe com leite:
    def test_buscar_por_cafe_com_leite(self):
        response = client.get('/client/?search=cafe+com+leite')
        self.assertEqual(response.content, b'[{"id":1,"chef":1,"receita":"cafe com leite"},{"id":4,"chef":2,"receita":"cafe com leite"}]')

    # Testa buscar receitas por macarrao com queijo:
    def test_buscar_por_macarrao_com_queijo(self):
        response = client.get('/client/?search=macarrao+com+queijo')
        self.assertEqual(response.content, b'[{"id":2,"chef":1,"receita":"macarrao com queijo"},{"id":5,"chef":2,"receita":"macarrao com queijo"}]')

    # Testa buscar receitas por suco de laranja:
    def test_buscar_por_suco_de_laranja(self):
        response = client.get('/client/?search=suco+de+laranja')
        self.assertEqual(response.content, b'[{"id":3,"chef":1,"receita":"suco de laranja"},{"id":6,"chef":2,"receita":"suco de laranja"}]')

        # Testa buscar receitas por lasanha:
    def test_buscar_por_lasanha(self):
        response = client.get('/client/?search=lasanha')
        self.assertEqual(response.content, b'[{"id":7,"chef":4,"receita":"lasanha"}]')


    # Testando filtrar por chef e buscar por texto da receita:

        # Testa filtrar por chef 1 e buscar receita cafe com leite:
    def test_filtrar_chef_1_e_buscar_receita_cafe_com_leite(self):
        response = client.get('/client/?chef=1&search=cafe+com+leite')
        self.assertEqual(response.content, b'[{"id":1,"chef":1,"receita":"cafe com leite"}]')

        # Testa filtrar por chef 2 e buscar receita cafe com leite:
    def test_filtrar_chef_2_e_buscar_receita_cafe_com_leite(self):
        response = client.get('/client/?chef=2&search=cafe+com+leite')
        self.assertEqual(response.content, b'[{"id":4,"chef":2,"receita":"cafe com leite"}]')
        

    # Testando tratamento de erros:    

        # Testa filtrar por chef 2 e buscar receita não cadastrada:
    def test_filtrar_chef_2_e_buscar_receita_nao_cadastrada(self):
        response = client.get('/client/?chef=2&search=receita+nao+cadastrada')
        self.assertEqual(response.content, b'[]')

        # Testa filtrar por chef que não está cadastrado e buscar receita cafe com leite:
    def test_filtrar_chef_nao_cadastrado_e_buscar_receita_cafe_com_leite(self):
        response = client.get('/client/?chef=100&search=cafe+com+leite')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Testa buscar receitas por receita que não está cadastrada:
    def test_buscar_por_receita_nao_cadastrada(self):
        response = client.get('/client/?search=receita+nao+cadastrada')
        self.assertEqual(response.content, b'[]')

        # Testa filtrar chef que não está cadastrado:
    def test_chef_que_nao_esta_cadastrado(self):
        response = client.get('/client/?chef=100')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
        # Testa filtrar chef que não está cadastrado e buscar receita que não existe:
    def test_chef_que_nao_esta_cadastrado_e_receita_nao_cadastrada(self):
        response = client.get('/client/?chef=100&search=receita+nao+cadastrada')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    
