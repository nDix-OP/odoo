from odoo import fields, models
from .data_type import DataType as Dt
from .status import Status as St


class GlossaryTerm(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = 'datagov.glossary.term'
    _description = 'Glossary term'

    # atributos mapeados
    id = fields.Id('Id', required=True)  # defecto es falso, id lo crea solo pero esta bien tenerlo tambien aqui
    name = fields.Text('Name')
    status = fields.Selection(selection=[  # lista valor - etiqueta
        (St.VIGENTE.name, 'Vigente'),
        (St.RETIRADO.name, 'Retirado'),
        (St.PROPUESTO.name, 'Propuesto')
    ], string='Status')
    description = fields.Text('Description')
    # clase # TODO
    # owner # TODO
    logical_model = fields.Text('LogicalModel')
    physical_model = fields.Text('PhysicalModel')
    data_type = fields.Selection(selection=[  # lista valor - etiqueta
        (Dt.ESTRUCTURADOS.name, 'Estructurados'),
        (Dt.SEMIESTRUCTURADOS.name, 'Semiestructurados'),
        (Dt.NO_ESTRUCTURADOS.name, 'No estructurados')
    ], string='Data type')
