from odoo import fields, models
from .data_type import DataType as Dt
from .status import Status as St


class GlossaryTerm(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = 'datagov.glossary.term'
    _description = 'Glossary term'
    _sql_constraints = [  # los check o unique
        ('name_unique', 'unique(name)', 'El atributo "Nombre" (name) debe ser único')
    ]

    # atributos mapeados
    id = fields.Id('Id', required=True)  # defecto es falso, id lo crea solo pero esta bien tenerlo tambien aqui
    name = fields.Text('Nombre')
    status = fields.Selection(selection=[  # lista valor - etiqueta
        (St.CURRENT.name, 'Vigente'),
        (St.NOT_IN_FORCE.name, 'Retirado'),
        (St.PROPOSED.name, 'Propuesto')
    ], string='Estatus')
    # TODO faltan atributos
    owner = fields.Many2one("datagov.actor", "Owner of this term")
    logical_model = fields.Text('Modelo lógico')
    physical_model = fields.Text('Modelo físico')
    data_type = fields.Selection(selection=[  # lista valor - etiqueta
        (Dt.STRUCTURED.name, 'Estructurados'),
        (Dt.SEMISTRUCTURED.name, 'Semiestructurados'),
        (Dt.UNSTRUCTURED.name, 'No estructurados')
    ], string='Tipo de dato')
