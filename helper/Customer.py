# -*- coding: utf-8 -*-
#!/usr/bin/env python

import requests

from Config import *

class Customer(object):
    def __init__(self, MAIN_PATH):
        self.CONFIG = get_info_environment(MAIN_PATH+'/config/moip_conf', 'QA')
        #self.endpoint = self.CONFIG['host'] + ":" + str(self.CONFIG['port'])
        self.endpoint = self.CONFIG['host']
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': 'BASIC U0hBOVBVS09TUE4xSlNDSTgyWFpMTEpEQ1pMTkpITkQ6TE9KRDlQS1hQWTkxQ0FWVUhKTTc0WEpQUUMwWTY2TU1UQkxURVNFUQ=='}


    def post_create_new_customer(self, ownId, fullname,email, birthDate, taxDocumentType, taxDocumentCpfNumber, phone_countryCode,
                                                             phone_areaCode,phone_number, shippingAddress_city,
                                                             shippingAddress_complement, shippingAddress_district,
                                                             shippingAddress_street, shippingAddress_streetNumber,
                                                             shippingAddress_zipCode, shippingAddress_state,
                                                             shippingAddress_country):

        payload = self.generate_payloads_create_new_customer(ownId, fullname, email, birthDate, taxDocumentType, taxDocumentCpfNumber, phone_countryCode,
                                                             phone_areaCode,phone_number, shippingAddress_city,
                                                             shippingAddress_complement, shippingAddress_district,
                                                             shippingAddress_street, shippingAddress_streetNumber,
                                                             shippingAddress_zipCode, shippingAddress_state,
                                                             shippingAddress_country)

        response = requests.post(self.endpoint + self.CONFIG['resource_customers'],
                                 headers=self.headers, data=json.dumps(payload))
        return response

    def get_list_customer_by_ownId(self, ownId):
        response = requests.get(self.endpoint + self.CONFIG['resource_customers'] + "/" + str(ownId) + "?limit=1",
                                headers=self.headers)
        return response

    def get_list_customers_filter_by_fullname(self, fullname):
        response = requests.get(self.endpoint + self.CONFIG['resource_customers'] + "?q=" + str(fullname) + "&limit=1",
                                headers=self.headers)
        return response


    def post_create_new_customer_with_credit_card(self, ownId, fullname, email, birthDate,taxDocumentTypeCpf,
                                              taxDocumentCpfNumber, phoneCountryCode, phoneAreaCode, phoneNumber,
                                              shippingAdressCity, shippingAdressComplement, shippingAdressDistrict,
                                              shippingAdressStreet, shippingAdressStreetNumber, shippingAdressZipCode,
                                              shippingAdressState, shippingAdressCountry, fundingInstrumentMethod,
                                                          CreditCardExpMonth, CreditCardExpYear, CreditCardNumber,
                                                          CreditCardCvc):

        payload = self.generate_payloads_create_new_customer_credit_card(ownId, fullname, email, birthDate,taxDocumentTypeCpf,
                                              taxDocumentCpfNumber, phoneCountryCode, phoneAreaCode, phoneNumber,
                                              shippingAdressCity, shippingAdressComplement, shippingAdressDistrict,
                                              shippingAdressStreet, shippingAdressStreetNumber, shippingAdressZipCode,
                                              shippingAdressState, shippingAdressCountry, fundingInstrumentMethod,
                                                          CreditCardExpMonth, CreditCardExpYear, CreditCardNumber,
                                                          CreditCardCvc)

        response = requests.post(self.endpoint + self.CONFIG['resource_customers'],
                                 headers=self.headers, data=json.dumps(payload))

        return response



    def generate_payloads_create_new_customer(self, ownId, fullname, email, birthDate,taxDocumentTypeCpf,
                                              taxDocumentCpfNumber, phoneCountryCode, phoneAreaCode, phoneNumber,
                                              shippingAdressCity, shippingAdressComplement, shippingAdressDistrict,
                                              shippingAdressStreet, shippingAdressStreetNumber, shippingAdressZipCode,
                                              shippingAdressState, shippingAdressCountry):

        return {"ownId": ownId, "fullname": fullname, "email": email, "birthDate": birthDate,
         "taxDocument": {"type": taxDocumentTypeCpf, "number": taxDocumentCpfNumber},
         "phone": {"countryCode": phoneCountryCode, "areaCode": phoneAreaCode, "number": phoneNumber},
         "shippingAddress": {"city": shippingAdressCity, "complement": shippingAdressComplement, "district": shippingAdressDistrict,
                             "street": shippingAdressStreet, "streetNumber": shippingAdressStreetNumber, "zipCode": shippingAdressZipCode,
                             "state": shippingAdressState, "country": shippingAdressCountry}}


    def generate_payloads_create_new_customer_credit_card(self, ownId, fullname, email, birthDate,taxDocumentTypeCpf,
                                              taxDocumentCpfNumber, phoneCountryCode, phoneAreaCode, phoneNumber,
                                              shippingAdressCity, shippingAdressComplement, shippingAdressDistrict,
                                              shippingAdressStreet, shippingAdressStreetNumber, shippingAdressZipCode,
                                              shippingAdressState, shippingAdressCountry, fundingInstrumentMethod,
                                                          CreditCardExpMonth, CreditCardExpYear, CreditCardNumber,
                                                          CreditCardCvc):

        return {"ownId": ownId, "fullname": fullname, "email": email, "birthDate": birthDate,
         "taxDocument": {"type": taxDocumentTypeCpf, "number": taxDocumentCpfNumber},
         "phone": {"countryCode": phoneCountryCode, "areaCode": phoneAreaCode, "number": phoneNumber},
         "shippingAddress": {"city": shippingAdressCity, "complement": shippingAdressComplement, "district": shippingAdressDistrict,
                             "street": shippingAdressStreet, "streetNumber": shippingAdressStreetNumber, "zipCode": shippingAdressZipCode,
                             "state": shippingAdressState, "country": shippingAdressCountry},
                "fundingInstrument": {"method": fundingInstrumentMethod, "creditCard": {
                       "expirationMonth": CreditCardExpMonth, "expirationYear": CreditCardExpYear,
                       "number": CreditCardNumber, "cvc": CreditCardCvc,
                       "holder": {"fullname": fullname, "birthdate": birthDate,
                                  "taxDocument": {"type": taxDocumentTypeCpf, "number": taxDocumentCpfNumber},
                                  "billingAddress": {
                                      "city": shippingAdressCity,
                                      "district": shippingAdressDistrict,
                                      "street": shippingAdressStreet,
                                      "streetNumber": shippingAdressStreetNumber,
                                      "zipCode": shippingAdressZipCode,
                                      "state": shippingAdressState,
                                      "country": shippingAdressCountry
                                  },
                                  "phone": {
                                      "countryCode": phoneCountryCode,
                                      "areaCode": phoneAreaCode,
                                      "number": phoneNumber
                                  }
                                  }
                   }
                                         }
                   }
