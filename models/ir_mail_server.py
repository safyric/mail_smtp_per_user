# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ir_mail_server(models.Model):
    _inherit = "ir.mail_server"

    user_id = fields.Many2one('res.users', string="Owner", help="If this is personal mail server choose owner.")
    #to do
    #is_user_mail_server = fields.Boolean(string="Mass Mailing Server", help="Use this mail server for mass mailing.")

    @api.model
    def send_email(self, message, mail_server_id=None, smtp_server=None, smtp_port=None,
                   smtp_user=None, smtp_password=None, smtp_encryption=None, smtp_debug=False):

        #get uid from context
        uid=self.env.context.get('uid')

        #if uid is None get uid from env
        if uid is None:
            uid=self.env.uid

        #if mail server has owner use that mail server
        mail_server = self.search([('user_id', '=', uid)], limit=1)
        if mail_server:
            mail_server_id = mail_server.id

        return super(ir_mail_server, self).send_email(message=message, mail_server_id=mail_server_id, smtp_server=smtp_server, smtp_port=smtp_port,
                   smtp_user=smtp_user, smtp_password=smtp_password, smtp_encryption=smtp_encryption, smtp_debug=smtp_debug)
