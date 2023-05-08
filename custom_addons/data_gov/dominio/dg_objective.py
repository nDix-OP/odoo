"""
Clase de domino de Objetivo de Gobernanza de Datos, se persiste automáticamente en la BD.
"""
import datetime

from .category_type import CategoryType
from odoo import fields, models, api
from odoo.exceptions import UserError


class DgObjective(models.Model):  # subclase de esta para persistir automáticamente en BD
    id = fields.Id('Id', required=True)
    name = fields.Text('Nombre', required=True)
    date = fields.Datetime('Fecha', required=True, default=datetime.datetime.now())
    description = fields.Text('Descripción', required=True)
    category = fields.Many2one('datagov.category', 'Categoría', required=True)  # clase Category
    owner = fields.Many2one('datagov.actor', 'Owner', required=True)  # many2one (tabla BD, descripcion)
    actor = fields.Many2one('datagov.actor', 'Actor responsable', required=True)

    # TODO el campo metric, una vez se haga la clase KPI

    # ---------------------------------------- Atributos privados ---------------------------------
    #  para la base de datos, no se muy bien que son cada una
    _name = 'datagov.dg.objective'  # nombre de la tabla BD
    _description = 'Objetivo de Gobernanza de Datos'
    _order = 'id desc'  # orden del indice por defecto
    _sql_constraints = [  # los check o unique
        ('name_unique', 'unique(name)', 'El atributo "Nombre" (name) debe ser único')
    ]

    # restricción de que la categoría sea de DG OBJECTIVE
    @api.onchange('category')
    def check_category(self):
        if self.category.type != CategoryType.DG_OBJECTIVE and self.category.name is not False:
            self.category = False  # dejar el valor anterior
            # lanzar notificación
            raise UserError("La categoría del objetivo de gobernanza de datos debe ser una del tipo " +
                            "'Objetivo Gob. datos'.")
        return
