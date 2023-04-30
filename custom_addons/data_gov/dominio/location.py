from odoo import fields, models


class Location(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = "datagov.location"
    _description = "Location, used for actors"
    # para que se busque por nombre en los dropdown
    _rec_name = 'locationName'

    id = fields.Text("Id", required=True)
    locationName = fields.Text("Nombre")
    locationAddress = fields.Text("Dirección")
