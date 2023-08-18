from odoo import models, fields

class CrmLead(models.Model):
    _inherit = "crm.lead"

    opportunity_type = fields.Selection(
        selection = [
            ('p_racks', 'Racks'),
            ('p_automatizacion', 'Automatizacion'),
            ('p_repuesto', 'Partes y Repuestos'),
            ('s_modificación','Armado, Movilizacion y Modificacion'),
            ('s_inspeccion','Inspeccion'),             
        ],
        string = "Type",
        required = True,
        index = True,
        copy = True,
        store = True
        )