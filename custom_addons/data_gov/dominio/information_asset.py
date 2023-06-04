from odoo import fields, models, api
from odoo.exceptions import UserError
from .category_type import CategoryType


class InformationAsset(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = 'datagov.information.asset'
    _description = 'Information Asset'
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

    # Atributos de relaciones con otras clases del modelo
    # TODO policy
    # TODO requirement (pero no se añade desde este lado)
    dataEntities =\
        fields.Many2many(relation='datagov_data_entity_information_asset', comodel_name='datagov.data.entity',
                         column1='id_data_entity', column2='id_information_asset', string='Elementos de datos')
    # TODO para cuando se tengan las 3
    dataQualityRule = fields.One2many('datagov.data.quality.rule', 'name', string='Reglas de calidad')

    # Many2many para information asset TODO
    '''performs = fields.Many2many(comodel_name='datagov.role', relation='datagov_role_actor', column1='id_actor',
                                column2='id_role', string='Roles')'''

    # restricción
    @api.onchange('category')
    def on_change_category(self):
        # comparar con el __eq__, si se pone vacío no salta pero después no deja guardar
        if self.category.type != CategoryType.INFORMATION_ASSET and self.category.name is not False:
            self.category = False  # dejar el valor anterior
            # lanzar notificación
            raise UserError("La categoría del actor debe ser una del tipo 'Activo de información'.")
        return

    @api.depends
    def check_tiene_entidades(self):
        if len(self.dataEntities.ids) == 0:
            raise UserError("El activo de información debe contener a, al menos, una entidad de datos.")
