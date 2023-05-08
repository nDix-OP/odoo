from odoo import fields, models, api
from odoo.exceptions import UserError
from .category_type import CategoryType


class Actor(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = 'datagov.actor'
    _description = 'Data Governance Actor'
    _sql_constraints = [  # los check o unique
        ('name_unique', 'unique(name)', 'El atributo "Nombre" (name) debe ser único')
    ]

    id = fields.Id('Id', required=True)
    name = fields.Text('Nombre', required=True)
    category = fields.Many2one('datagov.category', 'Categoría', required=True)  # clase Category
    description = fields.Text('Description', required=True)
    organizationUnit = fields.Many2one('datagov.organization.unit', 'Unidad organizativa', required=True)
    location = fields.Many2one('datagov.location', 'Localización', required=True)
    # aunque se use Many2one y de ese tipo, no se crean FK en la BD
    owner = fields.Many2one('datagov.actor', 'Owner del actor')   # IMPORTANTE: no requerido para poder añadir uno
    # Many2many
    performs = fields.Many2many(comodel_name='datagov.role', relation='datagov_role_actor', column1='id_actor',
                                column2='id_role', string='Roles')
    # One2many (otra tabla, atributo otra clase y description), poner many2one en la otra clase
    objective = fields.One2many('datagov.dg.objective', 'actor', string='Objetivos como responsable')

    # restricción de que la categoría sea de actor
    @api.onchange('category')
    def on_change_category(self):
        # comparar con el __eq__, si se pone vacío no salta pero después no deja guardar
        if self.category.type != CategoryType.ACTOR and self.category.name is not False:
            self.category = False  # dejar el valor anterior
            # lanzar notificación
            raise UserError("La categoría del actor debe ser una del tipo 'Actor'.")
        return
