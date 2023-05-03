from odoo import fields, models


class Location(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = "datagov.location"
    _description = "Location, used for actors"
    # para que se busque por nombre en los dropdown
    _rec_name = 'locationName'

    _sql_constraints = [  # los check o unique
        ('locationName_unique', 'unique(locationName)', 'El atributo "Nombre" (locationName) debe ser único')
    ]

    id = fields.Id("Id", required=True)
    locationName = fields.Text("Nombre", required=True)
    locationAddress = fields.Text("Dirección", required=True)
