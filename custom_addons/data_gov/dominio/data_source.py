from odoo import fields, models


class DataSource(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = 'datagov.data.source'
    _description = 'Data source'
    '''
    # atributos mapeados
    id = fields.Id('Id', required=True)
    name = fields.Text('Name')
    steward = fields.Text # TODO
    description = fields.Text('Description')
    clase # TODO
    owner # TODO
    logical_model = fields.Text('LogicalModel')
    physical_model = fields.Text('PhysicalModel')
    data_type = # TODO
    '''