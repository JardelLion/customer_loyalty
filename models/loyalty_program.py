from odoo import fields, models


class LoyaltyProgram(models.Model):
    _inherit = "loyalty.program"

    use_order_total_for_points = fields.Boolean(
        string="Calculate Points From Order Total",
        help=(
            "Award one point for every 10 monetary units "
            "of the sales order total."
        ),
    )