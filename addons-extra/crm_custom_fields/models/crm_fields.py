from odoo import models, fields

class CrmLead(models.Model):
    _inherit = "crm.lead"

    opportunity_type = fields.Char(
        string = "Type",
        required = True,
        index = True,
        copy = True,
        store = True
        )