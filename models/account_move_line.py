from odoo import api, fields, models


class AccountMoveLine(models.Model):
   _inherit = 'account.move.line'

   @api.onchange('partner_id')
   def _onchange_partner_id(self):
      if self.partner_id:
         account = self.env['res.partner'].search([('id', '=', self.partner_id.id)])

         for rec in account:
            return {'domain': {'account_id':['|',('id', '=', rec.property_account_receivable_id.id), ('id', '=', rec.property_account_payable_id.id)]}}

