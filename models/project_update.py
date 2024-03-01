# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import re
from odoo import _, models, fields, api


class ProjectUpdateReportInherit(models.Model):
    _inherit = ['project.update']

    attendees = fields.Many2many('res.partner')
    check_paste_attendees = fields.Boolean(default=False)
    paste_attendees = fields.Text()

    @api.onchange('paste_attendees')
    def onchange_paste_attendees(self):
        if self.paste_attendees:
            self.process_attendees()

    def process_attendees(self):
        email_pattern = r'([\w\s]+) <([\w\.-]+@[\w\.-]+)>'
        attendees = self.paste_attendees
        attendees_found = re.findall(email_pattern, attendees)
        existing_partners = self.env['res.partner'].search(
            [('email', 'in', [email for name, email in attendees_found])])
        new_partners = []
        for name, email in attendees_found:
            if email not in existing_partners.mapped('email'):
                partner = self.env['res.partner'].create({'name': name, 'email': email})
                existing_partners |= partner
                new_partners.append(partner)
        self.attendees = [(6, 0, existing_partners.ids)]
        self.check_paste_attendees = False
