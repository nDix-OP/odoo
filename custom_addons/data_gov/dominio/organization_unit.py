from odoo import fields, models


class OrganizationUnit(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = "datagov.organization.unit"
    _description = "Organization Unit, used for actor"

    # Decir que atributo se usa en los dropdown para buscar cuando se use como FK (como org del actor)
    # Por defecto es 'name' y por eso no hay que tocarlo en otros objetos como actor
    _rec_name = 'organizName'

    id = fields.Text("Id", required=True)
    organizName = fields.Text("Nombre")
    organizDescription = fields.Text("Descripción")
