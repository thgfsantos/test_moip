# -*- coding: utf-8 -*-
#!/usr/bin/env python

import random
import string
import os
from helper import Customer, Orders

MAIN_PATH = os.path.abspath(os.path.dirname(__file__))

class TestFunctionalOrders(object):
    @classmethod
    def setup_class(self):
        self.reqCustomer = Customer.Customer(MAIN_PATH)
        self.reqOrders = Orders.Orders(MAIN_PATH)
        self.orderId = "0"

    def test_create_new_customer(self):
        # Cenario de Teste: Cadastramento de um novo cliente com todos os parametros preenchidos.
        # Como resultado: Receber status code 201 e receber o ID unico do cliente

        temp_ownId = self.gen_customerId()
        response = self.reqCustomer.post_create_new_customer(temp_ownId, "Test Orders", "moip@moip.com.br",
                                                             "1990-10-22", "CPF", "22288866644", "55", "11",
                                                             "55552266", "São Paulo", "10", "Itaim Bibi",
                                                             "Avenida Faria Lima","500", "01234000", "SP", "BRA")

        resp_temp = response.json()
        assert response.status_code == 201

        assert resp_temp['ownId'] == temp_ownId

        self.customerId = resp_temp['id']


    def test_create_new_order(self):
        #Cenario: Criar um novo pedido associado a um cliente
        #Resultado: Criar um novo pedido e obter seu ID, status code 201.

        temp_ownId = self.gen_customerId()
        response_c = self.reqCustomer.post_create_new_customer(temp_ownId, "Test Orders", "moip@moip.com.br",
                                                             "1990-10-22", "CPF", "22288866644", "55", "11",
                                                             "55552266", "São Paulo", "10", "Itaim Bibi",
                                                             "Avenida Faria Lima", "500", "01234000", "SP", "BRA")

        resp_temp_c = response_c.json()
        self.customerId = resp_temp_c['id']

        response = self.reqOrders.post_create_new_order(temp_ownId, "BRL",  1500, "Descrição do pedido",
                                                        "CLOTHING",  1, "Camiseta estampada branca",
                                                        9500, self.customerId)

        resp_temp = response.json()
        assert response.status_code == 201

        assert resp_temp['ownId'] == temp_ownId
        assert resp_temp['status'] == "CREATED"
        assert resp_temp['items'][0]['category'] == "CLOTHING"
        assert resp_temp['items'][0]['detail'] == "Camiseta estampada branca"

        self.orderId = resp_temp['id']


    def test_consult_order_created(self):
        #Cenario: Consultar um pedido realizado por um cliente
        #Resultado: Obter informacoes do pedido cadastrado e status code 200.

        temp_ownId = self.gen_customerId()
        response_c = self.reqCustomer.post_create_new_customer(temp_ownId, "Test Orders", "moip@moip.com.br",
                                                               "1990-10-22", "CPF", "22288866644", "55", "11",
                                                               "55552266", "São Paulo", "10", "Itaim Bibi",
                                                               "Avenida Faria Lima", "500", "01234000", "SP", "BRA")

        resp_temp_c = response_c.json()
        self.customerId = resp_temp_c['id']

        response_o = self.reqOrders.post_create_new_order(temp_ownId, "BRL", 1500, "Descrição do pedido",
                                                        "CLOTHING", 1, "Camiseta estampada branca",
                                                        9500, self.customerId)

        resp_temp_o = response_o.json()
        self.orderId = resp_temp_o['id']
        temp_orderId = self.orderId

        response = self.reqOrders.get_consult_orders_created_by_orderId(temp_orderId)

        resp_temp = response.json()
        assert response.status_code == 200


        assert resp_temp['ownId'] == temp_ownId
        assert resp_temp['status'] == "CREATED"
        assert resp_temp['items'][0]['category'] == "CLOTHING"
        assert resp_temp['items'][0]['detail'] == "Camiseta estampada branca"

    def test_consult_order_no_exist(self):
        # Cenario: Criar um novo pedido com orderID nao existente
        # Resultado: Nao sera possivel criar um novo pedido com sucesso, status code 400 e info sobre o erro.

        non_orderId = "ORD-"+str(random.randint(1, 999999))

        response = self.reqOrders.get_consult_orders_created_by_orderId(non_orderId)

        assert response.status_code == 404


    def test_consult_blank_order(self):
        # Cenario: Criar um novo pedido com orderID nulo
        # Resultado: Nao sera possivel criar um novo pedido com sucesso, status code 400 e info sobre o erro.

        response = self.reqOrders.get_consult_orders_created_by_orderId("")

        temp = response.json()

        assert response.status_code == 200

    def test_create_new_order_with_product_desc_moreThan_250_caracter(self):
        # Cenario: Criar um novo pedido com a descricao do produto com mais de 250 caracteres permitidos.
        # Resultado: Nao sera possivel criar um novo pedido com sucesso, status code 400 e info sobre o erro.

        response = self.reqOrders.post_create_new_order("CUS-7387872842", "BRL", 1500, self.gen_random_string(251),
                                                        "CLOTHING", 1, "Camiseta estampada branca",
                                                        9500, "CUS-123")
        temp = response.json()

        assert response.status_code == 400
        assert temp['errors']

    def test_create_new_order_hight_quantity(self):
        # Cenario: Criar um novo pedido com orderID e uma quantidade maior do que a permitida.
        # Resultado: Nao sera possivel criar um novo pedido com sucesso, status code 400 e info sobre o erro.

        qtde = random.randint(10, 999999999999)

        temp_ownId = self.gen_customerId()
        response = self.reqOrders.post_create_new_order(temp_ownId, "BRL", 1500, "Descrição do pedido",
                                                        "CLOTHING", str(qtde), "Camiseta estampada branca",
                                                        9500, "CUS-123")
        temp = response.json()
        assert temp['errors']

        assert response.status_code == 400

    def test_create_new_order_hight_price(self):
        # Cenario: Criar um novo pedido com orderID e com valor do price maior do que o permitido.
        # Resultado: Nao sera possivel criar um novo pedido com sucesso, status code 400 e info sobre o erro.

        price = random.randint(1, 999999999999)
        temp_ownId = self.gen_customerId()

        response = self.reqOrders.post_create_new_order(temp_ownId, "BRL", 1500, "Descrição do pedido",
                                                        "CLOTHING", 1, "Camiseta estampada branca",
                                                        price, "CUS-123")
        temp = response.json()

        assert temp['errors']
        assert response.status_code == 400

    def gen_random_string(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def gen_customerId(self):
        return "CUS-" + str(random.randint(1, 999999999999))