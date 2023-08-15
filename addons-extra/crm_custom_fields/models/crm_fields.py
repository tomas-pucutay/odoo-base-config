from odoo import models, fields

class CrmLead(models.Model):
    _inherit = "crm.lead"

    opportunity_type = fields.Char(
        string = "Opportunity type",
        required = True,
        index = True,
        copy = True,
        store = True
        )