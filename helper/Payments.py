# -*- coding: utf-8 -*-
#!/usr/bin/env python

import requests

from Config import *

class Payments(object):
    def __init__(self, MAIN_PATH):
        self.CONFIG = get_info_environment(MAIN_PATH + '/config/moip_conf', 'QA')
        self.endpoint = self.CONFIG['host']
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': 'BASIC U0hBOVBVS09TUE4xSlNDSTgyWFpMTEpEQ1pMTkpITkQ6TE9KRDlQS1hQWTkxQ0FWVUhKTTc0WEpQUUMwWTY2TU1UQkxURVNFUQ=='}

    def post_create_new_payments_method_boleto(self, orderId, DescNameStore, PayMethod, boletoExpirationDate,
                                            boletoInstrFirstLine, boletoInstrSecondLine,
                                            boletoInstrThirdLine, logoUri):

        payload = self.generate_payloads_payment_by_boleto(DescNameStore, PayMethod, boletoExpirationDate,
                                            boletoInstrFirstLine, boletoInstrSecondLine,
                                            boletoInstrThirdLine, logoUri)

        response = requests.post(self.endpoint + self.CONFIG['resource_orders']+"/"+orderId+"/"+self.CONFIG['resource_payments'],
                                 headers=self.headers, data=json.dumps(payload))
        return response

    def post_create_new_payments_method_debit(self, orderId, PayMethod, BankDebitNumber, ExpiratationDate):

        payload = self.generate_payloads_payment_by_debit_card(PayMethod, BankDebitNumber, ExpiratationDate)

        response = requests.post(self.endpoint + self.CONFIG['resource_orders'] + "/" + orderId + "/" + self.CONFIG['resource_payments'],
                                 headers=self.headers, data=json.dumps(payload))
        return response

    def get_list_of_payments(self, paymentId):
        response = requests.get(self.endpoint + self.CONFIG['resource_payments']+"/"+paymentId,
                                headers=self.headers)
        return response

    def generate_payloads_payment_by_boleto(self, DescNameStore, PayMethod, boletoExpirationDate,
                                            boletoInstrFirstLine, boletoInstrSecondLine,
                                            boletoInstrThirdLine, logoUri):

        return {"statementDescriptor": DescNameStore, "fundingInstrument": {"method": PayMethod, "boleto": {
            "expirationDate": boletoExpirationDate, "instructionLines": {"first": boletoInstrFirstLine,
                                                                         "second": boletoInstrSecondLine,
                                                                         "third": boletoInstrThirdLine},
            "logoUri": logoUri}}}

    def generate_payloads_payment_by_debit_card(self, PayMethod, BankDebitNumber, ExpiratationDate):
        return {"fundingInstrument": {"method": PayMethod,
                                         "onlineBankDebit": {"bankNumber": int(BankDebitNumber),
                                                             "expirationDate": ExpiratationDate}}}
