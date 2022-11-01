from email.policy import default
from odoo import fields,models,api,_

class DentistAppointment(models.Model):
    _name = 'dentist.appointment'
    _description = 'Dentist Appointment'
    _inherit=['mail.thread','mail.activity.mixin']

    parent_id = fields.Many2one('dentist.patient',string='Patient',required=True)
    age = fields.Integer(string='Age',related='parent_id.pat_age')
    gender = fields.Selection(string='Gender',related='parent_id.pat_gender')
    note = fields.Text(string='Note')
    date_appointment = fields.Date(string='Date')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancel')], default='draft', string='status', tracking=True)

    reference = fields.Char(string="Order Reference",required=True,copy=False,readonly=True,default=lambda self: _('New'))

    def action_confirm(self):
        self.state ='confirm'


    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'


    def action_cancel(self):
        self.state = 'cancel'

    @api.model
    def create(self, vals_list):
        #check if patient age field is empty
        if not vals_list.get('note'):
            vals_list['note'] = 'New Appointment Created '

        if vals_list.get('reference', _('New')) == _('New'):
            vals_list['reference'] = self.env['ir.sequence'].next_by_code('dentist.appointment') or _('New')

        res = super(DentistAppointment,self).create(vals_list)
        return res

    @api.onchange('parent_id')
    def onchange_parent_id(self):
        if self.parent_id :
            self.note = 'New Appointment Created For ' + self.parent_id.name
        else :
            self.note = ''
