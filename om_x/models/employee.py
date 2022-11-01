from odoo import models,fields,api

class HrEmployee(models.Model):
    _inherit=['hr.employee']

    em_prenom = fields.Char(string="Prénom" ,  required =True)
    em_matricule = fields.Char(string="Matricule")
    em_cin = fields.Char(string="N° CIN"  ,required =True)

    #em_direction_generale = fields.Selection(selection=[('Direction Generale A','Direction Generale A'),('Direction Generale B','Direction Generale B')],string='Direction Generale')
    #em_pole = fields.Selection([('Pole A','Pole B')],string='Pole')
    #em_departement = fields.Selection(selection= [('a','a')],string='Departement')
    #em_service = fields.Selection(selection= [('a','a')],string='Service')
    #em_equipe = fields.Selection([('a','a')],string='Equipe')
    #em_agent = fields.Selection([('a','a')],string='Agent')

    dir_gen = fields.Many2one('direction.generale', string="xx", required=True)

    #@api.onchange('dir_gen')
    #def onchange_dir_gen(self):
    #    print(self.dir_gen)
    #    if self.dir_gen.name == 'Direction Generale A':
    #        print('ab')
    #        dir_gen.em_pole = fields.Selection(selection_add=[('Pole A', 'Pole A'), ('Pole B', 'Pole B')])
    #    elif self.dir_gen.name == 'Direction Generale B':
    #        print('CD')
    #        dir_gen.em_pole = fields.Selection(selection=[('Pole C', 'Pole C'), ('Pole D', 'Pole D')], string='Pole')
#
    #def TestFunction(self):
    #    #self.em_pole =self.em_pole.append(("new option","new option"))
    #    self.em_pole = fields.Selection(selection_add=[('transgender', 'Transgender')])
    #    print('nooooooooooooooooooooooooooooooooooooooooooo')

class DirectionGenerale(models.Model):
    _name = 'direction.generale'

    name = fields.Selection(selection=[('Direction Generale A','Direction Generale A'),('Direction Generale B','Direction Generale B')],string='Direction Generale')

    @api.onchange('name')
    def onchange_dir_gen(self):
        if self.name=='Direction Generale A':
            self.em_pole = fields.Selection([('a','a')],string='Pole')
        elif name == 'Direction Generale B':
            self.em_pole = fields.Selection([('b','b')],string='Pole')

    #em_departement = fields.Selection(selection= [('a','a')],string='Departement')
    #em_service = fields.Selection(selection= [('a','a')],string='Service')
    #em_equipe = fields.Selection([('a','a')],string='Equipe')
    #em_agent = fields.Selection([('a','a')],string='Agent')

