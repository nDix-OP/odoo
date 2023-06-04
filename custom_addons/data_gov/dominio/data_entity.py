from odoo import fields, models, api
from odoo.exceptions import UserError
from .category_type import CategoryType


class DataEntity(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = 'datagov.data.entity'
    _description = 'Data Entity'
    _sql_constraints = [  # los check o unique
        ('name_unique', 'unique(name)', 'El atributo "Nombre" (name) debe ser único')
    ]

    id = fields.Id('Id', required=True)
    name = fields.Text('Nombre', required=True)
    category = fields.Many2one('datagov.category', 'Categoría', required=True)  # clase Category
    description = fields.Text('Descripción', required=True)
    securityClassification = fields.Many2one('datagov.security.classification', 'Clasificación de seguridad',
                                             required=True)
    steward = fields.Many2one('datagov.actor', 'Administrador', required=True)
    isDigital = fields.Boolean('Es digital', required=True)
    lineage = fields.Text('Linaje', required=True)
    # Atributos de relaciones con otras clases del modelo
    masterDataSource = fields.Many2one('datagov.data.source', 'Fuente de datos maestra', required=True)
    term = fields.Many2one('datagov.glossary.term', 'Término del glosario', required=True)
    dataElements = fields.One2many('datagov.data.element', 'dataEntity', string='Elementos de datos')
    informationAssets = \
        fields.Many2many(relation='datagov_data_entity_information_asset', comodel_name='datagov.information.asset',
                         column1='id_information_asset', column2='id_data_entity', string='Activos de información')
    # TODO para cuando se tengan las 3
    dataQualityRule = fields.One2many('datagov.data.quality.rule', 'name', string='Reglas de calidad')

    # LA AGREGACIÓN CONSIGO MISMA
    # Tiene que ser Many2Many a los dos lados para poder añadir tal y como queremos
    # Hay que crear un atributo adicional oculto para la padre, pero esconderlo en las vistas, limite de un elemento
    compone = fields.Many2many(relation='datagov_data_entity_aggregation', comodel_name='datagov.data.entity',
                               column1='id_compone', column2='id_padre', string='Entidad que compone')
    composedOf = fields.Many2many(relation='datagov_data_entity_aggregation', comodel_name='datagov.data.entity',
                                  column1='id_padre', column2='id_compone', string='Compuesta por')

    # restricción
    @api.onchange('category')
    def on_change_category(self):
        # comparar con el __eq__, si se pone vacío no salta pero después no deja guardar
        if self.category.type != CategoryType.DATA_ENTITY and self.category.name is not False:
            self.category = False  # dejar el valor anterior
            # lanzar notificación
            raise UserError("La categoría del actor debe ser una del tipo 'Entidad de datos'.")
        return

    # Que la relación consigo para la agregación siga siendo 1-N
    @api.onchange('composedOf')
    def _check_many2many_limit(self):
        lista_compone = self.compone.ids  # hay que obtener la lista con los id, el método len() no va con many2many
        lista_compuesta = self.composedOf.ids
        # hay que pasar por cada una de las que lo componen para comprobar esto
        for comp_id in lista_compuesta:
            obj = self.env['datagov.data.entity'].browse(comp_id)  # obtener objeto completo, no la parte de inner join
            # print('ID:', obj.name, 'Compone: ', str(obj.compone.ids), ' len: ', len(obj.compone))
            if len(obj.compone) > 0:  # 0 porque en este punto no contiene la que se va a añadir
                texto_error = 'Una entidad de datos no puede ser parte de la composición de dos o más entidades (' + \
                    obj.name + ').'
                raise UserError(texto_error)
        # que si eres una entidad compuesta no puedas componer otras y viceversa
        if len(lista_compuesta) > 0 and len(lista_compone) > 0:
            raise UserError('Una entidad de datos compuesta no puede ser parte de otras entidades.')
        # que no sea consigo misma
        if self.compone.__contains__(self):
            raise UserError('Una entidad de datos no puede ser compuesta por sí misma.')
