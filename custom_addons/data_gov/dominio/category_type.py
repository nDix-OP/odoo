from enum import Enum


class CategoryType(Enum):
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
