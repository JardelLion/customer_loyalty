from odoo import models, fields, api, exceptions, _

class LoyaltyCardInherit(models.Model):
    _inherit = 'loyalty.card'

    @api.constrains('points')
    def _check_manual_points_permission(self):
        if not self.env.user.has_group('customer_loyalty.group_loyalty_card'):
            raise exceptions.AccessError(_('Only users in the Loyalty card group can manually change points.'))