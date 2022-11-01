from email.policy import default
from odoo import fields,models,api,_

class DentistPatient(models.Model):
    _name = 'dentist.patient'
    _description = 'Dentist Management System'
    _inherit=['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Full Name')
    pat_age = fields.Integer(string='Age')
    pat_gender = fields.Selection([('male','Male'),('female','Female')],string='Gender')
    pat_img = fields.Binary(string='Image')
    pat_responsible = fields.Many2one(comodel_name='res.partner',string='Responsible')

    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancel')], default='draft', string='status', tracking=True)
    reference = fields.Char(string="Order Reference",required=True,copy=False,readonly=True,default=lambda self: _('New'))
    appointment_count = fields.Integer(string='Total Appointment',compute='_compute_appointment_count')

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
        if not vals_list.get('pat_age'):
            vals_list['pat_age'] = 18

        if vals_list.get('reference', _('New')) == _('New'):
            vals_list['reference'] = self.env['ir.sequence'].next_by_code('dentist.patient') or _('New')

        res = super(DentistPatient,self).create(vals_list)
        return res


    def _compute_appointment_count(self):
        #total_appointment = self.env['dentist.appointment'].search_count([('parent_id', '=', self.id)])
        #print('self.name')
        self.appointment_count = 10