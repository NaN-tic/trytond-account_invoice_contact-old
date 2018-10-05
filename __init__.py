#This file is part account_invoice_contact module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool
from . import address
from . import invoice

def register():
    Pool.register(
        address.Address,
        invoice.Invoice,
        module='account_invoice_contact', type_='model')
