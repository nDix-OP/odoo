from odoo import fields, models
from . import category_type as tipo


class Category(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = "datagov.category"
    _description = "Category type"

    id = fields.Text("Id", required=True)
    name = fields.Text("Name")
    description = fields.Text("Description")
    type = fields.Selection(selection=[  # lista valor - etiqueta
        ("IA", tipo.CategoryType.IA.name),
        ("DGOBJECTIVE", tipo.CategoryType.DGOBJECTIVE.name),
        ("KPI", tipo.CategoryType.KPI.name),
        ("POLICY", tipo.CategoryType.POLICY.name),
        ("PROCEDURE", tipo.CategoryType.PROCEDURE.name),
        ("PRINCIPLE", tipo.CategoryType.PRINCIPLE.name),
        ("QUALITY", tipo.CategoryType.QUALITY.name),
        ("TERM", tipo.CategoryType.TERM.name)
    ],
        string="Category Type")
