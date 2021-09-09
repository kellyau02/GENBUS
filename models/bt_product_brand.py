# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class bt_product_brand(models.Model):
    _name = "bt.product.brand"
    _description = "Brand"
    _rec_name = "brand"
    _order = "brand"
    _check_company_auto = True

    company_id = fields.Many2one('res.company', required=True,
                                 index=True, default=lambda self: self.env.company)

    brand = fields.Char(string='Brand')
    active = fields.Boolean(string='Active', default=True)

