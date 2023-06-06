from odoo import fields, models, api
from odoo.exceptions import UserError


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

    # los Many2One que hay que poner como many2many para que se puedan escoger desde las otras clases
    # solo uno puede ser no nulo a la vez, y solo un valor
    dataElement = fields.Many2many(relation='datagov_data_element_rule', comodel_name='datagov.data.element',
                                   column1='id_regla', column2='id_elemento', string='Elemento de datos que la aplica')
    dataEntity = fields.Many2many(relation='datagov_data_entity_rule', comodel_name='datagov.data.entity',
                                  column1='id_regla', column2='id_entidad', string='Entidad de datos que la aplica')
    informationAsset =\
        fields.Many2many(relation='datagov_information_asset_rule', comodel_name='datagov.information.asset',
                         column1='id_regla', column2='id_activo', string='Activo de información que la aplica')

    dataQualityRequirement = fields.Many2one('datagov.data.quality.requirement', 'Requisito de calidad de datos',
                                             required=True)

    # este método se copia en la entidad, activo y elemento para cuando se inserta desde ahí
    @api.onchange('dataElement', 'dataEntity', 'informationAsset')
    def on_change_many2many(self):
        if self.id:  # si hay id
            i = self.id
            # más cómodo si se ejecuta la query conjunta
            query = "SELECT id_regla, id_elemento FROM datagov_data_element_rule WHERE id_regla = " + str(i) + \
                    " UNION SELECT id_regla, id_entidad FROM datagov_data_entity_rule WHERE id_regla = " + str(i) + \
                    " UNION SELECT id_regla, id_activo FROM datagov_information_asset_rule WHERE id_regla = " + str(i)
            self.env.cr.execute(query)
            resultado = self.env.cr.fetchall()
            if len(resultado) > 0:  # no incluye el actual
                texto = "La regla de calidad de datos ya está asignada a otro activo de información, entidad o " \
                        "elemento, y solo puede estar asignada a uno."
                raise UserError(texto)
