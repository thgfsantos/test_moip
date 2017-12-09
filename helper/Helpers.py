# -*- coding: utf-8 -*-
#!/usr/bin/env python

class Helpers(object):
    def __init__(self):
        self.ownId = ""
        self.customerId = ""
        self.orderId = ""
        self.paymentId = ""

    def set_ownId(self, temp_ownId):
        self.ownId = temp_ownId

    def set_customerId(self, temp_customerId):
        self.customerId = temp_customerId

    def set_orderId(self, temp_orderId):
        self.orderId = temp_orderId

    def set_paymentId(self, temp_payment):
        self.paymentId = temp_payment

    def get_ownId(self):
        return self.ownId

    def get_customerId(self):
        return self.customerId

    def get_orderId(self):
        return self.orderId

    def get_paymentId(self):
        return self.paymentId
