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
        email_pattern = r'([\w\s\.]+)\s*<([\w\.-]+@[\w\.-]+)>'
        email_only_pattern = r'([\w\.-]+@[\w\.-]+)'

        entries = self.paste_attendees.split(',')
        attendees_found = []

        for entry in entries:
            match = re.search(email_pattern, entry.strip())
            if match:
                attendees_found.append(match.groups())
            else:
                lone_emails = re.findall(email_only_pattern, entry.strip())
                attendees_found.extend([(None, email) for email in lone_emails])

        for name, email in attendees_found:
            if email:
                partner = self.env['res.partner'].search([('email', '=', email.strip())], limit=1)
                if partner:
                    if name and partner.name == 'Desconocido':
                        partner.name = name.strip()
                else:
                    name_to_use = name.strip() if name else 'Unknown'
                    partner = self.env['res.partner'].create({'name': name_to_use, 'email': email.strip()})
                    self.attendees |= partner

        self.paste_attendees = ''

        self.check_paste_attendees = False
