from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _program_check_compute_points(self, programs):
        self.ensure_one()

        # Preserve the native Odoo loyalty calculations.
        result = super()._program_check_compute_points(programs)

        for program in programs:
            if not program.use_order_total_for_points:
                continue

            # Preserve the native eligibility checks.
            program_result = result.get(program, {})
            if "error" in program_result:
                continue

            # One point for every 10 monetary units.
            points = int(self.amount_total / 10)

            # Keep the native coupon creation, wallet update
            # and loyalty history mechanisms.
            program_result["points"] = [points]

        return result