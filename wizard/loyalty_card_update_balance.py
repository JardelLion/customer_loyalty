# -*- coding: utf-8 -*-
from odoo import models, api, _
from odoo.exceptions import AccessError


class LoyaltyCardUpdateBalance(models.TransientModel):
    _inherit = 'loyalty.card.update.balance'

    @api.model
    def default_get(self, fields_list):
        """ Validates the group immediately upon opening the Wizard. """
        res = super().default_get(fields_list)
        if not self.env.user.has_group('customer_loyalty.group_loyalty_card'):
            raise AccessError(_("Only users belonging to the 'Loyalty Card' group can change the point balance.."))
        return res

    def action_update_card_point(self):
        """ Ensures the group is verified when clicking the confirmation button. """
        if not self.env.user.has_group('customer_loyalty.group_loyalty_card'):
            raise AccessError(_("Only users belonging to the 'Loyalty Card' group can change the point balance.."))
        
        return super().action_update_card_point()