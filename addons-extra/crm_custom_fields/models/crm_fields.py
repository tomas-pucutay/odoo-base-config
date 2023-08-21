from odoo import models, fields

class CrmLead(models.Model):
    _inherit = "crm.lead"

    op_category = fields.Selection(
        selection = [
            ('p_racks', 'Racks'),
            ('p_automatizacion', 'Automatizacion'),
            ('p_repuesto', 'Partes y Repuestos'),
            ('s_modificación', 'Armado, Movilizacion y Modificacion'),
            ('s_mantenimiento', 'Mantenimiento de Equipos'),
            ('s_inspeccion', 'Inspeccion'),
            ('otros', 'Otros')
        ],
        string = "Category",
        index = True,
        copy = True,
        store = True
        )
    
    op_analytic_account = fields.Many2one(
        comodel_name="account.analytic.account",
        string="Analytic Account",
        index = True,
        copy = True,
        store = True
    )