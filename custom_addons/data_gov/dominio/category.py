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
    type = fields.Selection(selection=[  # lista valor - etiqueta
        (tipo.CategoryType.IA.name, tipo.CategoryType.IA.value),
        (tipo.CategoryType.DGOBJECTIVE.name, tipo.CategoryType.DGOBJECTIVE.value),
        (tipo.CategoryType.KPI.name, tipo.CategoryType.KPI.value),
        (tipo.CategoryType.POLICY.name, tipo.CategoryType.POLICY.value),
        (tipo.CategoryType.PROCEDURE.name, tipo.CategoryType.PROCEDURE.value),
        (tipo.CategoryType.PRINCIPLE.name, tipo.CategoryType.PRINCIPLE.value),
        (tipo.CategoryType.QUALITY.name, tipo.CategoryType.QUALITY.value),
        (tipo.CategoryType.TERM.name, tipo.CategoryType.TERM.value)
    ],
        string="Tipo de categoría", required=True)

    _sql_constraints = [  # los check o unique
        ('name_unique', 'unique(name)', 'El atributo "Nombre" (name) debe ser único')
    ]
