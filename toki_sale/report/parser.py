
# -*- coding: utf-8 -*- 


import logging 
logger = logging.getLogger('report_aeroo') 
from openerp.report import report_sxw 
from openerp.report.report_sxw import rml_parse 


class Parser(rml_parse): 
    def __init__(self, cr, uid, name, context): 
        super(self.__class__, self).__init__(cr, uid, name, context) 
        self.localcontext.update({ 
            'hello_world': self.hello_world, 
        }) 

    def hello_world(self, name): 
        return "Hello, %s!" % name

