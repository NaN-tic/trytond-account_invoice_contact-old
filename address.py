#This file is part account_invoice_contact module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['Address']
__metaclass__ = PoolMeta


class Address:
    __name__ = 'party.address'
    contact = fields.Boolean('Contact')
