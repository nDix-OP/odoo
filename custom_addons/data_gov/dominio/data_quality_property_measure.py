from odoo import fields, models, api
from .category_type import CategoryType


class DataQualityPropertyMeasure(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = 'datagov.data.quality.property.measure'
    _description = 'Data Quality Property Measure'
    _sql_constraints = [  # los check o unique
        ('name_unique', 'unique(name)', 'El atributo "Nombre" (name) debe ser único')
    ]

    # que herede del KPI y todos sus atributos
    _inherit = 'datagov.kpi'

    # renombrar estas tablas para que no salte error
    disseminatedTo = fields.Many2many(relation='datagov_property_measure_disseminated_to', comodel_name='datagov.actor',
                                      column1='id_property_measure', column2='id_actor', string='Difundido a')
    inputParameter = fields.Many2many(relation='datagov_property_measure_input_parameter',
                                      comodel_name='datagov.input.parameter',
                                      column1='id_property_measure', column2='id_parameter',
                                      string='Parámetros de entrada')
    policy = fields.Many2many(relation='datagov_policy_property_measure', comodel_name='datagov.policy',
                              column1='id_property_measure', column2='id_policy', string='Políticas')

    # insertar atributos y relaciones adicionales de la subclase
    category = fields.Many2one('datagov.category', 'Categoría', required=True,
                               default='Medida de calidad de datos', readonly=True)

    dataQualityRequirement = \
        fields.Many2many(relation='datagov_data_quality_property_measure_requirement',
                         comodel_name='datagov.data.quality.requirement',
                         column1='id_property_measure', column2='id_requirement',
                         string='Requisitos de calidad de datos')

    dataQualityCharacteristic = fields.Many2one('datagov.data.quality.characteristic',
                                                'Característica de calidad de datos', required=True)
