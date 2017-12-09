# -*- coding: utf-8 -*-
#!/usr/bin/env python

import requests

from Config import *

class Orders(object):
    def __init__(self, MAIN_PATH):
        self.CONFIG = get_info_environment(MAIN_PATH + '/config/moip_conf', 'QA')
        self.endpoint = self.CONFIG['host']
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': 'BASIC U0hBOVBVS09TUE4xSlNDSTgyWFpMTEpEQ1pMTkpITkQ6TE9KRDlQS1hQWTkxQ0FWVUhKTTc0WEpQUUMwWTY2TU1UQkxURVNFUQ=='}

    def post_create_new_order(self, ownId, amountCurrency, subTotalShipping, itemsProductDesc,
                                 itemsProductCategory, itemsProductQuantity, itemsProductDetail,
                                 itemsProductPrice, customerId):

        payload = self.generate_payloads_orders(ownId, amountCurrency, subTotalShipping, itemsProductDesc,
                                                itemsProductCategory, itemsProductQuantity, itemsProductDetail,
                                                itemsProductPrice, customerId)

        response = requests.post(self.endpoint + self.CONFIG['resource_orders'],
                                 headers=self.headers, data=json.dumps(payload))
        return response


    def get_consult_orders_created_by_orderId(self, orderId):

        response = requests.get(self.endpoint + self.CONFIG['resource_orders']+"/"+orderId, headers=self.headers)

        return response


    def generate_payloads_orders(self, ownId, amountCurrency, subTotalShipping, itemsProductDesc,
                                 itemsProductCategory, itemsProductQuantity, itemsProductDetail,
                                 itemsProductPrice, customerId):

        return {"ownId": ownId, "amount": {"currency": amountCurrency, "subtotals": {"shipping": int(subTotalShipping)}},
                   "items": [{"product": itemsProductDesc, "category": itemsProductCategory, "quantity": int(itemsProductQuantity),
                              "detail": itemsProductDetail,
                              "price": itemsProductPrice}], "customer": {"id": customerId}}