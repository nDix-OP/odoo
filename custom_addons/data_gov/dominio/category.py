from odoo import fields, models
from . import category_type as tipo


class Category(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = "datagov.category"
    _description = "Category type"
    _order = "id DESC"

    id = fields.Id("Id", required=True)
    name = fields.Text("Nombre", required=True)
    description = fields.Text("Descripción", required=True)
    type = fields.Many2one('datagov.category.type', string="Tipo de categoría", required=True)

    _sql_constraints = [  # los check o unique
        ('name_unique', 'unique(name)', 'El atributo "Nombre" (name) debe ser único')
    ]
