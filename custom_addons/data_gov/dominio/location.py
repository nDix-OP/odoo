from odoo import fields, models


class Location(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = "datagov.location"
    _description = "Location, used for actors"
    # para que se busque por nombre en los dropdown
    # _rec_name = 'locationName'

    id = fields.Id("Id", required=True)
    name = fields.Text("Nombre")
    address = fields.Text("Dirección")

    _sql_constraints = [  # los check o unique
        ('name_unique', 'unique(name)', 'El atributo "Nombre" (name) debe ser único')
    ]
