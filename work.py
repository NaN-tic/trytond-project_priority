# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.

from trytond.model import fields
from trytond.pool import PoolMeta

__metaclass__ = PoolMeta
__all__ = ['Work']


class Work:
    __name__ = 'project.work'

    priority = fields.Selection([
            ('100', 'Very Low'),
            ('250', 'Low'),
            ('500', 'Normal'),
            ('750', 'High'),
            ('1000', 'Very High')], 'Priority', select=True)

    @staticmethod
    def default_priority():
        return '500'
