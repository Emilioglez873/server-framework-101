from odoo import models, fields, api


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate type"
    _order = "sequence,name"

    sequence = fields.Integer()
    name = fields.Char(required=True)
    property_ids = fields.One2many("estate.property", "property_type_id", string="Property types")
    offer_ids = fields.One2many("estate.property.offer", "property_type_id", string="Offers")
    offer_count = fields.Integer(compute="_compute_offer_count")

    _sql_constraints = [
        (
            'check_name_type', 'UNIQUE(name)',
            'The type should be unique'
        ),
    ]

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
