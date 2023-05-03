from enum import Enum
from odoo import models


class CategoryType(Enum):
    '''
    _name = 'datagov.category.type'
    _description = 'Tipo de categoría'
    _rec_name = 'value'  # para que en la interfaz muestre el texto
    '''

    INPUT_PARAMETER = 'Parámetro de entrada'
    ROLE = 'Rol'
    ACTOR = 'Actor'
    PRINCIPLE = 'Principio'
    SECURITY_CLASSIFICATION = 'Clasificación de seguridad'
    KPI = 'KPI'
    DG_OBJECTIVE = 'Objetivo Gob. datos'
    INFORMATION_ASSET = 'Activo de información'
    POLICY = 'Política'
    PROCEDURE = 'Procedimiento'
    DATA_ENTITY = 'Entidad de datos'
    GLOSSARY_TERM = 'Término del glosario'
