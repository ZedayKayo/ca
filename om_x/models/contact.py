from odoo import models,fields

class ResPartner(models.Model):
    _inherit= 'res.partner'

    con_prenom = fields.Char(string="Prénom" ,  required =True)
    con_n_cin = fields.Char(string="N° CIN", required =True)
