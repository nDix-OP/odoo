from odoo import fields, models


class Location(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = "datagov.location"
    _description = "Location, used for actors"

    id = fields.Text("Id", required=True)
    locationName = fields.Text("Location name")
    locationAddress = fields.Text("Address")