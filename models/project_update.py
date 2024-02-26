# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, models, fields


class ProjectUpdateReportInherit(models.Model):
    _inherit = ['project.update']

    attendees = fields.Many2many('res.partner')
