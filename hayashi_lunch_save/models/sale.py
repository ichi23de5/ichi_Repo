from openerp import api, fields ,models, _

class SaleOrder(models.Model):
	_inherit = "sale.order"

	relation_ids = fields.One2many('hayashi','mainmenu_id',string='Tabelog')

