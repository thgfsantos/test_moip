# -*- coding: utf-8 -*-
#!/usr/bin/env python

import pytest

pytest.main(["-s", "moip2/test_payments.py", "moip2/test_customers.py", "moip2/test_orders.py"])

