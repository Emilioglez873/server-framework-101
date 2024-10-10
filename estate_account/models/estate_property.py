from odoo import models, Command


class EstatePropertyInherited(models.Model):

    _inherit = "estate.property"

    def action_sold(self):

        result = super().action_sold()
        invoice_vals = {
            "partner_id": self.buyer_id.id,
            "move_type": "out_invoice",
            "line_ids": [
                Command.create(
                    {"name": "Selling price commission", "quantity": 1, "price_unit": self.selling_price * 0.06}
                ),
                Command.create({"name": "Admisnitrative fees ", "quantity": 1, "price_unit": 100.00}),
            ],
        }
        self.env["account.move"].create(invoice_vals)
        return result
