from odoo import fields, models


class Actor(models.Model):
    # nombre de la tabla de la BD (convierte . a _)
    _name = 'datagov.actor'
    _description = 'Data Governance Actor'

    id = fields.Text('Id', required=True)
    name = fields.Text('Nombre')
    category = fields.Many2one('datagov.category', 'Categoría')  # clase Category
    description = fields.Text('Descripción')
    organizationUnit = fields.Many2one('datagov.organization.unit', 'Unidad organizativa')
    location = fields.Many2one('datagov.location', 'Localización')
    # aunque se use Many2one y de ese tipo, no se crean FK en la BD
    owner = fields.Many2one('datagov.actor', 'Owner del actor')   # many2one (tabla BD, descripcion)
    # Many2many
    inChargeOf = fields.Many2many(comodel_name='datagov.role', relation='datagov_role_actor', column1='id_actor',
                                  column2='id_role', string='Roles')

    ''' De momento obvio este atributo para no poner mas tablas
    # One2many (otra tabla, atributo otra clase y descripcion), poner many2one en la otra clase
    objective = fields.One2many('datagov.dgobjective', 'actor', 'Objetivo de los que es responsable')
    '''