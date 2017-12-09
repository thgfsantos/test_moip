# -*- coding: utf-8 -*-
#!/usr/bin/env python

import random
import os

from helper import Customer, Orders, Payments

MAIN_PATH = os.path.abspath(os.path.dirname(__file__))

class TestFunctionPayments(object):

    @classmethod
    def setup_class(self):
        self.reqCustomer = Customer.Customer(MAIN_PATH)
        self.reqOrders = Orders.Orders(MAIN_PATH)
        self.reqPayments = Payments.Payments(MAIN_PATH)


    def test_create_new_payments_method_boleto(self):
        #Cenario: Criar um novo pagamento como forma de pagamento em Boleto com um pedido associado.
        #Resultado: Criar um ordem de pagamento com sucesso, status code 201 e obter o id do pagamento.

        temp_orderId = self.get_orderId()

        response = self.reqPayments.post_create_new_payments_method_boleto(str(temp_orderId), "Minha Loja", "BOLETO",
                                                                           "2020-06-20", "Atenção,",
                                                                           "fique atento à data de vencimento do boleto.",
                                                                           "Pague em qualquer casa lotérica.",
                                                                           "http://www.thiagopresentes.com.br/thgpres.jpg")
        temp = response.json()

        assert response.status_code == 201

    def test_create_new_payments_method_debit(self):
        # Cenario: Criar um novo pagamento como forma de pagamento em Cartao de Debito com um pedido associado.
        # Resultado: Criar um ordem de pagamento com sucesso, status code 201 e obter o id do pagamento.

        temp_orderId = self.get_orderId()

        response = self.reqPayments.post_create_new_payments_method_debit(temp_orderId, "ONLINE_BANK_DEBIT",
                                                                          341, "2017-12-08")
        temp = response.json()
        print temp

        assert response.status_code == 201

    def test_create_new_payments_with_non_exist_orderId(self):
        # Cenario: Criar um novo pagamento como forma de pagamento em Boleto sem um pedido associado.
        # Resultado: Nao sera possivel criar uma ordem de pagamento com sucesso, status code 400 e info sobre o erro.

        response = self.reqPayments.post_create_new_payments_method_debit("ORD-ioio123", "ONLINE_BANK_DEBIT",
                                                                          341, "2017-12-08")
        temp = response.json()

        assert response.status_code == 400

    def test_create_new_payments_invalid_date_expiration(self):
        # Cenario: Criar um novo pagamento como forma de pagamento em Boleto com um pedido associado mas
        # data de expiracao invalida.
        # Resultado: Nao sera possivel criar uma ordem de pagamento com sucesso, status code 400 e info sobre o erro.

        temp_orderId = self.get_orderId()
        response = self.reqPayments.post_create_new_payments_method_debit(temp_orderId, "ONLINE_BANK_DEBIT",
                                                                          341, "")
        temp = response.json()

        assert response.status_code == 400

    def test_create_new_payments_with_non_exist_method_to_pay(self):
        # Cenario: Criar um novo pagamento como forma de pagamento nao cadastrada com um pedido associado.
        # Resultado: Nao sera possivel criar uma ordem de pagamento com sucesso, status code 400 e info sobre o erro.

        temp_orderId = self.get_orderId()
        response = self.reqPayments.post_create_new_payments_method_debit(temp_orderId, "MOIP",
                                                                          341, "2017-12-08")
        temp = response.json()

        assert response.status_code == 400

    def test_consult_payments(self):
        # Cenario: Consultar uma ordem de pagamento pelo seu ID e obter informacoes do mesmo.
        # Resultado: Obter informacoes do pagamento buscado.

        response = self.reqPayments.get_list_of_payments("")

        temp = response.json()

        assert response.status_code == 200

    def get_orderId(self):
        temp_ownId = self.gen_customerId()
        response_c = self.reqCustomer.post_create_new_customer(temp_ownId, "Test Orders", "moip@moip.com.br",
                                                               "1990-10-22", "CPF", "22288866644", "55", "11",
                                                               "55552266", "São Paulo", "10", "Itaim Bibi",
                                                               "Avenida Faria Lima", "500", "01234000", "SP", "BRA")

        resp_temp_c = response_c.json()
        temp_customerId = resp_temp_c['id']

        response_o = self.reqOrders.post_create_new_order(temp_ownId, "BRL", 1500, "Descrição do pedido",
                                                          "CLOTHING", 1, "Camiseta estampada branca",
                                                          9500, temp_customerId)

        resp_temp_o = response_o.json()
        return resp_temp_o['id']


    def gen_customerId(self):
        return "CUS-" + str(random.randint(1, 999999999999))
