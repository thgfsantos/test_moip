# -*- coding: utf-8 -*-
#!/usr/bin/env python

import pytest

pytest.main(["--disable-warnings", "test_moip/test_payments.py", "test_moip/test_customers.py", "test_moip/test_orders.py"])

