from odoo import fields, models


class DataElement(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = 'datagov.data.element'
    _description = 'Data Element'
    _sql_constraints = [  # los check o unique
        ('name_unique', 'unique(name)', 'El atributo "Nombre" (name) debe ser único')
    ]

    id = fields.Id('Id', required=True)
    name = fields.Text('Nombre', required=True)
    conceptualDomain = fields.Text('Dominio conceptual', required=True)
    valueDomain = fields.Text('Valor del dominio', required=True)

    # Atributos de relaciones con otras clases del modelo
    term = fields.Many2one('datagov.glossary.term', 'Término del glosario', ondelete='set null')
    # TODO para cuando estén todas, es many to many, y probar el set null
    dataQualityRule = fields.One2many('datagov.data.quality.rule', 'name', string='Reglas de calidad',
                                      ondelete='set null')
    # Hacer la composición con DataElement
    dataEntity = fields.Many2one('datagov.data.entity', 'Entidad  de datos que compone', required=True)
