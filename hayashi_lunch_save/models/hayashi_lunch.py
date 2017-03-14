# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime, timedelta
# Non-odoo library
# import random
# from random import randint
# import string


class HayashiLunch(models.Model):
    _name = 'hayashi'
    _order = 'date_report desc'

    mainmenu_id = fields.Char('menu', required=True, placeholder='title')
    gourmet_report = fields.Text(string='Tabelog')
    companion_id = fields.Many2one('res.users', string='companion')
    date_report = fields.Date(string='Report Date', required=True, readonly=True, index=True, copy=False, default=fields.Datetime.now)
    val_del = fields.Boolean(string='Delicious?')
    price_menu = fields.Integer(string='price', default=0)
    image_main = fields.Binary(string='picture', attachment=True,)
    opinion_type = fields.Selection([ 
        ('delicious', 'Yummy'), 
        ('average', 'Aberage'), 
        ('Bad', 'Yucky')],
        default='average') 
    test = fields.Char(string='Oyatsu', default='I wonder if I meet some nice tea.')
    test2 = fields.Boolean(string='Have a teatime?')
    relation_id = fields.Many2one('res.partner',string='Ralated Field M2O')
    relation2_id = fields.One2many('res.partner','id',string='Ralated Field O2M')
    relation3_id = fields.Many2one('res.users',string='Ralated Users')
    relation4_id = fields.Many2one('sale.order',string='Ralated SaleOrder')
#    relation5_id = fields.Many2one('res.partner',string='Ralated Field M2O')
    relation6_id = fields.Many2one('product.product',string='Ralated Product')
#    relation7_id = fields.Many2one('res.partner',string='Ralated Field M2O')
    relation8_id = fields.Many2one('purchase.order',string='Ralated PurchaseOrder')




####This field is for StatusBar #####
####Need some code to xml <field name ="state" widget="statusbar"###### 
    state = fields.Selection([
        ('hunger', 'Im hungry'),
        ('normal', 'I dont want to eat'),
        ('full', 'Im full'),
        ('locked', 'I can take anymore!'),
        ], string='Status', readonly=True, default='hunger')
#    calorie = fields.Integer(string="Calirie", compute="_compute_calorie")
##### Using if else state ######
#    @api.onchange('test2') 
#    def _test_change(self):
#        if self.test2:
#            self.update({'test':"Good taste tea!"})
#        else:            
#            self.update({'test':"All I need a cup of tea!!!"})
#        return


###### Using variable msg ########
#    @api.onchange('test2')
#    def _test_change(self):
#        if not self.test2:
#            return
#        if self.test2:
#            msg = "How hot tea!"
#            self.update({'test': msg})
#        return


##### Adding Strings variable###########
#    @api.onchange('test2')
#    def _test_change(self):
#        if not self.test2:
#            return
#        else:
#            msg = "How hot tea! "
#            msg2 = "Please give me some water!"
#            self.update({'test': msg + msg2})
#        return



##### Adding Interger variable###########
#    @api.onchange('test2')
#    def _test_change(self):
#        if not self.test2:
#            return
#        else:
#            int = 10
#            int2 = 20

##### Adding Interger variable###########
#    @api.onchange('test2')
#    def _test_change(self):
#        if not self.test2:
#            return
#        else:
#            int = 10
#            int2 = 20
#            self.update({'test': int + int2})
#        return
#            self.update({'test': int + int2})
#        return


##### Checking List or Dict inside###########
#    @api.onchange('test2')
#    def _test_change(self):
#        if not self.test2:
#            return
#        else:
#            pp = self
#            self.update({'gourmet_report': pp})
#         
#        return



##### if Push Button then Change a comment.###########
#    @api.multi
#    def function_a(self):
#        self.ensure_one()
#        self.gourmet_report = "You push down the function A button!!"
#        return
#
#    @api.multi
#    def function_b(self):
#        self.ensure_one()
#        self.price_menu = 2000
#        return
#
#
#    @api.multi
#    def function_c(self):
#        self.ensure_one()
#        self.opinion_type = "delicious"
#        return


##### Using write() method ###########
    @api.multi
    def function_a(self):
        self.ensure_one()
        self.gourmet_report = "You push down the function A button!!"
        return

    @api.multi
    def function_b(self):
        self.ensure_one()
        self.price_menu = 2000
        return


    @api.multi
    def function_c(self):
        self.write({'test':'Can you see?'})
        return

#    @api.depends()
#    def _compute_calorie(self):
#        pass









#        vals = {} 
#        domain = {'test': [('test2', '=', self.product_id.uom_id.category_id.id)]} 
#        if not self.product_uom or (self.product_id.uom_id.id != self.product_uom.id): 
#            vals['product_uom'] = self.product_id.uom_id 
#            vals['product_uom_qty'] = 1.0 
