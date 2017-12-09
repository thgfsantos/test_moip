# -*- coding: utf-8 -*-
#!/usr/bin/moip_conf python

import random
import string
import os

from helper import Customer, Helpers
MAIN_PATH = os.path.abspath(os.path.dirname(__file__))

class TestFunctionalCustomer(object):

    @classmethod
    def setup_class(self):
        self.reqCustomer = Customer.Customer(MAIN_PATH)
        self.fullname = "Teste Moip"
        self.email = "test_moip@moip.com.br"
        self.birthDate = "1976-10-10"
        self.taxDocumentType = "CPF"
        self.taxDocumentCpfNumber = random.randint(1, 99999999999)
        self.phone_countryCode = "55"
        self.phone_areaCode = "11"
        self.phone_number = "56553466"
        self.shippingAddress_city = "São Paulo"
        self.shippingAddress_complement = "10"
        self.shippingAddress_district = "Itaim Bibi"
        self.shippingAddress_street = "Avenida Teste Moip"
        self.shippingAddress_streetNumber = "500"
        self.shippingAddress_zipCode = "01234000"
        self.shippingAddress_state = "SP"
        self.shippingAddress_country = "BRA"
        self.fundingInstrumentMethod = "CREDIT_CARD"
        self.CreditCardExpMonth = "10"
        self.CreditCardExpYear = "23"
        self.CreditCardNumber = str(random.randint(1, 9999999999999999))
        self.CreditCardCvc = "432"
        self.ownId = "0"
        self.customerId = "0"

    def test_create_new_customer(self):
        # Cenario de Teste: Cadastramento de um novo cliente com todos os parametros preenchidos.
        # Como resultado: Receber status code 201 e receber o ID unico do cliente

        temp_ownId = self.gen_customerId()
        self.ownId = str(temp_ownId)

        response = self.reqCustomer.post_create_new_customer(temp_ownId, self.fullname, self.email, self.birthDate,
                                                             self.taxDocumentType, self.taxDocumentCpfNumber,
                                                             self.phone_countryCode, self.phone_areaCode, self.phone_number,
                                                             self.shippingAddress_city,
                                                             self.shippingAddress_complement, self.shippingAddress_district,
                                                             self.shippingAddress_street, self.shippingAddress_streetNumber,
                                                             self.shippingAddress_zipCode, self.shippingAddress_state,
                                                             self.shippingAddress_country)

        assert response.status_code == 201

        resp_temp = response.json()

        assert resp_temp['ownId'] == str(self.ownId)
        assert resp_temp['fullname'] == self.fullname
        assert resp_temp['email'] == self.email


    def test_consult_customer_by_ownId(self):
        # Cenario para consultar um cliente recentemente criado.
        # Resultado esperado: status code 200 OK e informcoes sobre o cliente

        temp_ownId = self.gen_customerId()
        self.ownId = str(temp_ownId)

        response_c = self.reqCustomer.post_create_new_customer(temp_ownId, self.fullname, self.email, self.birthDate,
                                                             self.taxDocumentType, self.taxDocumentCpfNumber,
                                                             self.phone_countryCode, self.phone_areaCode,
                                                             self.phone_number,
                                                             self.shippingAddress_city,
                                                             self.shippingAddress_complement,
                                                             self.shippingAddress_district,
                                                             self.shippingAddress_street,
                                                             self.shippingAddress_streetNumber,
                                                             self.shippingAddress_zipCode, self.shippingAddress_state,
                                                             self.shippingAddress_country)

        resp_temp_c = response_c.json()
        self.customerId = resp_temp_c['id']

        temp_customId= self.customerId

        response = self.reqCustomer.get_list_customer_by_ownId(temp_customId)
        assert response.status_code == 200

        resp_temp = response.json()

        assert resp_temp['id'] == self.customerId()
        assert resp_temp['email'] == self.email
        assert resp_temp['ownId'] == temp_ownId

    def test_consult_customers(self):
        # cenario para realizar uma busca na listagem de clientes filtrando pelo full name do cliente
        # Resultado: Status code 200 e informacoes sobre o cliente dado seu full name

        response = self.reqCustomer.get_list_customers_filter_by_fullname(self.fullname)

        assert response.status_code == 200

        resp_temp = response.json()
        #assert resp_temp['customers'][0]['id'] == str(self.customerId)
        assert resp_temp['customers'][0]['email'] == self.email

    def test_create_new_customer_blank_OwnId(self):
        # Cenario: Criar um novo cliente com ownId null
        # Resultado: Nao deve ser permitido a criacao de clientes com ownId null

        response = self.reqCustomer.post_create_new_customer("", self.fullname, self.email, self.birthDate,
                                                             self.taxDocumentType, self.taxDocumentCpfNumber,
                                                             self.phone_countryCode, self.phone_areaCode, self.phone_number,
                                                             self.shippingAddress_city,
                                                             self.shippingAddress_complement, self.shippingAddress_district,
                                                             self.shippingAddress_street, self.shippingAddress_streetNumber,
                                                             self.shippingAddress_zipCode, self.shippingAddress_state,
                                                             self.shippingAddress_country)

        assert response.status_code == 400
        temp = response.json()
        assert temp['errors'][0]['code'] == "CUS-001"

    def test_create_new_customer_with_invalid_cpf(self):
        # Cenario: Criacao de um novo cliente com cpf invalido.
        # resultado: Nao deve permitir a criacao de cliente com cpf invalido maior que 12 digitos.

        temp_ownId = self.gen_customerId()
        response = self.reqCustomer.post_create_new_customer(temp_ownId, self.fullname, self.email, self.birthDate,
                                                             self.taxDocumentType, random.randint(1, 999999999999),
                                                             self.phone_countryCode, self.phone_areaCode,
                                                             self.phone_number,
                                                             self.shippingAddress_city,
                                                             self.shippingAddress_complement,
                                                             self.shippingAddress_district,
                                                             self.shippingAddress_street,
                                                             self.shippingAddress_streetNumber,
                                                             self.shippingAddress_zipCode, self.shippingAddress_state,
                                                             self.shippingAddress_country)
        assert response.status_code == 400

        temp = response.json()
        assert temp['errors'][0]['code'] == "PAY-036"

    def test_create_new_customer_with_fullname_moreThan_90_caracteres(self):
        # Cenario: criacao de um novo cliente com nome maior de 90 caracteres
        # Resultado: Nao deve permitir a criacao e retornar status code 400 e info de erro sobre fullname.
        # OBS: Este cenario ao executar retornar erro status code 500 do servidor

        temp_ownId = self.gen_customerId()
        response = self.reqCustomer.post_create_new_customer(temp_ownId, self.gen_random_string(91), self.email, self.birthDate,
                                                             self.taxDocumentType, self.taxDocumentCpfNumber,
                                                             self.phone_countryCode, self.phone_areaCode,
                                                             self.phone_number,
                                                             self.shippingAddress_city,
                                                             self.shippingAddress_complement,
                                                             self.shippingAddress_district,
                                                             self.shippingAddress_street,
                                                             self.shippingAddress_streetNumber,
                                                             self.shippingAddress_zipCode, self.shippingAddress_state,
                                                             self.shippingAddress_country)
        temp = response.json()
        assert temp['ERROR']
        assert response.status_code == 500

    def test_create_new_customer_OwnId_moreThan_65_caracteres(self):
        # Cenario: Criar novo cliente com OwnId com mais de 65 caracteres permitidos.
        # Resultado: Nao deve permitir a criacao retornando status code 400 e info de erro sobre ownId

        response = self.reqCustomer.post_create_new_customer(self.gen_random_string(66), self.fullname, self.email, self.birthDate,
                                                             self.taxDocumentType, self.taxDocumentCpfNumber,
                                                             self.phone_countryCode, self.phone_areaCode,
                                                             self.phone_number,
                                                             self.shippingAddress_city,
                                                             self.shippingAddress_complement,
                                                             self.shippingAddress_district,
                                                             self.shippingAddress_street,
                                                             self.shippingAddress_streetNumber,
                                                             self.shippingAddress_zipCode, self.shippingAddress_state,
                                                             self.shippingAddress_country)
        assert response.status_code == 500

        temp = response.json()
        assert temp['ERROR']

    def test_create_new_customer_with_credit_card(self):
        # Cenario: Cria um novo cliente com cartao de credito
        # Resultado: Criacao do novo cliente com cartao de credito e status code 201.

        temp_ownIdCredit = self.gen_customerId()

        response = self.reqCustomer.post_create_new_customer_with_credit_card(temp_ownIdCredit, self.fullname, self.email,
                                                                              self.birthDate,
                                                                              self.taxDocumentType,
                                                                              self.taxDocumentCpfNumber,
                                                                              self.phone_countryCode,
                                                                              self.phone_areaCode,
                                                                              self.phone_number,
                                                                              self.shippingAddress_city,
                                                                              self.shippingAddress_complement,
                                                                              self.shippingAddress_district,
                                                                              self.shippingAddress_street,
                                                                              self.shippingAddress_streetNumber,
                                                                              self.shippingAddress_zipCode,
                                                                              self.shippingAddress_state,
                                                                              self.shippingAddress_country,
                                                                              self.fundingInstrumentMethod,
                                                                              self.CreditCardExpMonth,
                                                                              self.CreditCardExpYear,
                                                                              self.CreditCardNumber,
                                                                              self.CreditCardCvc)
        assert response.status_code == 201

        resp_temp = response.json()
        assert resp_temp['ownId'] == temp_ownIdCredit
        assert resp_temp['email'] == self.email

    def test_create_new_customer_with_invalid_credit_card(self):
        temp_ownIdcredit = self.gen_customerId()

        response = self.reqCustomer.post_create_new_customer_with_credit_card(temp_ownIdcredit, self.fullname, self.email,
                                                                              self.birthDate,
                                                                              self.taxDocumentType,
                                                                              self.taxDocumentCpfNumber,
                                                                              self.phone_countryCode,
                                                                              self.phone_areaCode,
                                                                              self.phone_number,
                                                                              self.shippingAddress_city,
                                                                              self.shippingAddress_complement,
                                                                              self.shippingAddress_district,
                                                                              self.shippingAddress_street,
                                                                              self.shippingAddress_streetNumber,
                                                                              self.shippingAddress_zipCode,
                                                                              self.shippingAddress_state,
                                                                              self.shippingAddress_country,
                                                                              self.fundingInstrumentMethod,
                                                                              self.CreditCardExpMonth,
                                                                              self.CreditCardExpYear,
                                                                              str(random.randint(1, 999999999999999999)),
                                                                              self.CreditCardCvc)

        assert response.status_code == 400

        temp = response.json()

        assert temp['errors'][0]['code'] == "PAY-641"

    def gen_random_string(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def gen_customerId(self):
        return "CUS-" + str(random.randint(1, 999999999999))

