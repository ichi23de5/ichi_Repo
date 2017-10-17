# -*- coding: utf-8 -*-


from itertools import chain
import time

from openerp import tools
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT
from openerp.osv import fields, osv
from openerp.tools.translate import _

import openerp.addons.decimal_precision as dp
from openerp.exceptions import UserError
from openerp import api, models, fields as Fields


class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"


    @api.one
    @api.depends('categ_id', 'product_tmpl_id', 'product_id', 'compute_price', 'fixed_price', \
        'pricelist_id', 'percent_price', 'price_discount', 'price_surcharge')
    def _get_pricelist_item_name_price(self):
        if self.categ_id:
## Add code from here
            self.name = self._make_pricelistname(self.categ_id)
## Up to here
        elif self.product_tmpl_id:
            self.name = self.product_tmpl_id.name
        elif self.product_id:
            self.name = self.product_id.display_name.replace('[%s]' % self.product_id.code, '')
        else:
            self.name = _("All Products")

        if self.compute_price == 'fixed':
            self.price = ("%s %s") % (self.fixed_price, self.pricelist_id.currency_id.name)
        elif self.compute_price == 'percentage':
            self.price = _("%s %% discount") % (self.percent_price)
        else:
            self.price = _("%s %% discount and %s surcharge") % (abs(self.price_discount), self.price_surcharge)

## Add method 
    @api.multi
    def _make_pricelistname(self, ctg_id):
        cur_categ = ctg_id
        categ_name = ""
        if self.categ_id.id == 1 or self.categ_id.id == 2 or cur_categ.parent_id.id == 2:
            return self.categ_id.name
        else:
            cnt = 1
            while cur_categ.id <> 2:
                if cnt == 1:
                    categ_name = self.categ_id.parent_id.name + "/" + self.categ_id.name
                else:
                    if cur_categ.parent_id.id == 2:
                        return categ_name
                    else:
                        categ_name = cur_categ.parent_id.name +  "/" + categ_name
                cur_categ =  cur_categ.parent_id
                cnt = cnt + 1
            return categ_name


