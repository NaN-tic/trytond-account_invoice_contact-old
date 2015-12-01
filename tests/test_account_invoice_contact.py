# This file is part of the account_invoice_contact module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class AccountInvoiceContactTestCase(ModuleTestCase):
    'Test Account Invoice Contact module'
    module = 'account_invoice_contact'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        AccountInvoiceContactTestCase))
    return suite