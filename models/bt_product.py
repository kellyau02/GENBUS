# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class bt_product(models.Model):
    _inherit = "product.template"

    part_num = fields.Char(string='Part num')
    brand = fields.Many2one('bt.product.brand', string='Brand')

    _sql_constraints = [
        ('field_unique',
         'unique(part_num)',
         'This part number already exists - Enter another, it must be unique.')
    ]
