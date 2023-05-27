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
    description = fields.Text('Description', required=True)
    securityClassification = fields.Many2one('datagov.security.classification', 'Clasificación de seguridad',
                                             required=True)
    steward = fields.Many2one('datagov.actor', 'Administrador', required=True)
    isDigital = fields.Boolean('Es digital', required=True)
    lineage = fields.Text('Linaje', required=True)
    # Atributos de relaciones con otras clases del modelo
    masterDataSource = fields.Many2one('datagov.data.source', 'Fuente de datos maestra', required=True)
    term = fields.Many2one('datagov.glossary.term', 'Término del glosario', required=True)
    dataQualityRule = fields.One2many('datagov.data.quality.rule', 'name', string='Reglas de calidad')

    # Many2many para information asset
    '''performs = fields.Many2many(comodel_name='datagov.role', relation='datagov_role_actor', column1='id_actor',
                                column2='id_role', string='Roles')'''

    '''
    # One2many sobre la misma tabla para la agregación TODO ver como evitar recursión
    # Hay que crear un atributo adicional para la padre, pero esconderlo en las vistas
    parentEntity = fields.Many2one('datagov.data.entity', string='Entidad padre')  # la padre
    composedOf = fields.One2many('datagov.data.entity', 'name', string='Compuesta por')  # la compuesta
    '''

    # restricción
    @api.onchange('category')
    def on_change_category(self):
        # comparar con el __eq__, si se pone vacío no salta pero después no deja guardar
        if self.category.type != CategoryType.DATA_ENTITY and self.category.name is not False:
            self.category = False  # dejar el valor anterior
            # lanzar notificación
            raise UserError("La categoría del actor debe ser una del tipo 'Entidad de datos'.")
        return

    '''
    # que no pueda estar compuesta por si mismo
    @api.onchange('composedOf')
    def on_change_composed_of(self):
        for i in self.composedOf:
            # ver que no se ha metido si mismo
            if i.name == self.name:
                # lanzar notificación
                raise UserError("Una entidad de datos no puede estar compuesta por sigo misma.")
        return
    '''
