from odoo import fields, models


class DataQualityRule(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = 'datagov.data.quality.rule'
    _description = 'Data Quality Rule'
    _sql_constraints = [  # los check o unique
        ('name_unique', 'unique(name)', 'El atributo "Nombre" (name) debe ser único')
    ]

    # atributos mapeados
    id = fields.Id('Id', required=True)
    name = fields.Text('Nombre', required=True)
    description = fields.Text('Descripción', required=True)
    owner = fields.Many2one('datagov.actor', 'Propietario', required=True)   # many2one (tabla BD, descripción)
