from odoo import fields, models


class OrganizationUnit(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = "datagov.organization.unit"
    _description = "Organization Unit, used for actor"

    # Decir que atributo se usa en los dropdown para buscar cuando se use como FK (como org del actor)
    # Por defecto es 'name' y por eso no hay que tocarlo en otros objetos como actor
    _rec_name = 'organizName'

    id = fields.Id("Id", required=True)
    organizName = fields.Text("Nombre", required=True)
    organizDescription = fields.Text("Descripción", required=True)

    _sql_constraints = [  # los check o unique
        ('organizacion_unique', 'unique(organizName)', 'El atributo "Nombre" (organizName) debe ser único')
    ]
