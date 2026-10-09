from odoo import models, fields, api


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    loyalty_card_ids = fields.One2many('loyalty.card', 'partner_id', string='Carteiras de Fidelidade')
    total_loyalty_points = fields.Float(
        string='Total Points',
        compute='_compute_total_loyalty_points',
        store=True
    )
    loyalty_level = fields.Selection([
        ('bronze', 'Bronze'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
    ], string='Loyalty Level', compute='_compute_loyalty_level', store=True, default='bronze')

    @api.depends('loyalty_card_ids.points')
    def _compute_total_loyalty_points(self):
        for partner in self:
            partner.total_loyalty_points = sum(card.points for card in partner.loyalty_card_ids)

    @api.depends('total_loyalty_points')
    def _compute_loyalty_level(self):
        for partner in self:
            partner.upgrade_level()

    def upgrade_level(self):
        """ Requisito 6: Altera automaticamente o nível com base no total de pontos acumulados """
        for partner in self:
            points = partner.total_loyalty_points
            if points >= 5000:
                partner.loyalty_level = 'gold'
            elif points >= 1000:
                partner.loyalty_level = 'silver'
            else:
                partner.loyalty_level = 'bronze'

