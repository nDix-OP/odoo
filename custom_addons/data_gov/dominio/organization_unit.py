from odoo import fields, models


class OrganizationUnit(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = "datagov.organization.unit"
    _description = "Organization Unit, used for actor"

    id = fields.Text("Id", required=True)
    organizName = fields.Text("Nombre")
    organizDescription = fields.Text("Descripción")
