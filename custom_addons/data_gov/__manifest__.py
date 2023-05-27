# -*- coding: utf-8 -*-
# More info at https://www.odoo.com/documentation/master/reference/module.html

{
    "name": "Data Governance",
    "author": "Iván Ortiz del Noval",
    "category": 'Data/Technical',
    "depends": [
        "base",
        "web"
    ],
    "description": "Data governance utilities.",
    "data": [
        # rellenar con archivos, los csv o xml, ...
        "seguridad/ir.model.access.csv",  # permisos del modelo de dominio
        "vistas/datagov_categorias_views.xml",
        "vistas/datagov_actores_views.xml",
        "vistas/datagov_roles_views.xml",
        "vistas/datagov_data_sources_views.xml",
        "vistas/datagov_dgobjectives_views.xml",
        "vistas/datagov_ubicaciones_views.xml",
        "vistas/datagov_unidades_org_views.xml",
        "vistas/datagov_terminos_glosario_views.xml",
        "vistas/datagov_procedimientos_views.xml",
        "vistas/datagov_principios_views.xml",
        "vistas/datagov_reglas_calidad_datos_views.xml",
        "vistas/datagov_estandares_views.xml",
        "vistas/datagov_parametros_views.xml",
        "vistas/datagov_clasificacion_seguridad_views.xml",
        "vistas/datagov_entidades_datos_views.xml",
        "vistas/datagov_main_menu.xml",  # IMPORTANTE: ponerlo al final porque usa cosas de los otros xml de vistas
    ],
    "application": True,
    "license": "LGPL-3",
}
