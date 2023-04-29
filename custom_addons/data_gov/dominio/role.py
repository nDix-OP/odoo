"""
Clase de domino de Role, se persiste automáticamente en la BD.
"""

from odoo import fields, models


class Role(models.Model):  # subclase de esta para persistir automáticamente en BD
    id = fields.Text('Id', required=True)
    name = fields.Text('Name', required=True)
    mainTasks = fields.Text('Main tasks', required=True)
    profile = fields.Text('Profile', required=True)
    category = fields.Many2one('datagov.category', 'Category', required=True)  # clase Category
    skills = fields.Text('Skills', required=True)
    owner = fields.Many2one('datagov.actor', 'Owner', required=True)   # many2one (tabla BD, descripcion)
    # Many2many(otra tabla objeto, nombre tabla relacion, fkcolumna1, fkcolumna2, descripcion)
    performedBy = fields.Many2many(comodel_name='datagov.actor', relation='datagov_role_actor', column1='id_role',
                                   column2='id_actor', string='Actors with the role')

    # ---------------------------------------- Private Attributes ---------------------------------
    #  para la base de datos, no se muy bien que son cada una
    _name = 'datagov.role'  # nombre de la tabla BD
    _description = 'Rol'
    _order = 'id desc'  # orden del indice por defecto
    '''
    _sql_constraints = [  # los check TODO
        ('check_expected_price', 'CHECK(expected_price > 0)', 'The expected price must be strictly positive'),
        ('check_selling_price', 'CHECK(selling_price >= 0)', 'The offer price must be positive'),
    ]
    '''
    