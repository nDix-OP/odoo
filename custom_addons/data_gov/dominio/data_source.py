import datetime

from odoo import fields, models, api
from .data_source_class import DataSourceClass
from .data_type import DataType
from .status import Status


class DataSource(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = 'datagov.data.source'
    _description = 'Data source'
    _sql_constraints = [  # los check o unique
        ('name_unique', 'unique(name)', 'El atributo "Nombre" (name) debe ser único')
    ]

    # atributos mapeados
    id = fields.Id('Id', required=True)
    name = fields.Text('Name', required=True)
    steward = fields.Many2one('datagov.actor', 'Steward', required=True)
    description = fields.Text('Descripción', required=True)
    clase = fields.Selection(selection=[  # lista valor - etiqueta
        # no veo otra forma que poner uno a uno cada valor
        # hay que meter el nombre, no deja poniendo el objeto entero
        (DataSourceClass.SERVICIO_STREAMING.name, DataSourceClass.SERVICIO_STREAMING.value),
        (DataSourceClass.SERVIDOR_BD.name, DataSourceClass.SERVIDOR_BD.value),
        (DataSourceClass.SISTEMA_FICHEROS.name, DataSourceClass.SISTEMA_FICHEROS.value),
        (DataSourceClass.SISTEMA_TRANSFERENCIA_FICHEROS.name, DataSourceClass.SISTEMA_TRANSFERENCIA_FICHEROS.value),
        (DataSourceClass.API.name, DataSourceClass.API.value),
    ],
        string="Clase", required=True)  # en la vista no se puede modificar después
    owner = fields.Many2one('datagov.actor', 'Owner', required=True)
    logical_model = fields.Text('Modelo lógico', required=True)
    physical_model = fields.Text('Modelo físico', required=True)
    data_type = fields.Selection(selection=[  # lista valor - etiqueta
        (DataType.ESTRUCTURADOS.name, DataType.ESTRUCTURADOS.value),
        (DataType.SEMIESTRUCTURADOS.name, DataType.SEMIESTRUCTURADOS.value),
        (DataType.NO_ESTRUCTURADOS.name, DataType.NO_ESTRUCTURADOS.value),
    ],
        string="Tipo de datos", required=True)  # en la vista no se puede modificar después
    status = fields.Selection(selection=[  # lista valor - etiqueta
        (Status.VIGENTE.name, Status.VIGENTE.value),
        (Status.PROPUESTO.name, Status.PROPUESTO.value),
        (Status.RETIRADO.name, Status.RETIRADO.value),
    ],
        string="Estatus", required=True)
    statusDate = fields.Datetime('Fecha de estatus', required=True,
                                 default=datetime.datetime.now())  # se tiene que cambiar en onChange de status

    # como onChange pero solo se ejecuta al guardar, es para campos calculados
    # al cambiar el status, la fecha de modificación es la actual
    @api.onchange("status")
    def _compute_status_date(self):
        self.statusDate = fields.Datetime.now()
