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
        "vistas/datagov_actores_views.xml",
        "vistas/datagov_main_menu.xml",  # IMPORTANTE: ponerlo al final porque usa cosas de los otros xml de vistas
    ],
    "application": True,
    "license": "LGPL-3",
}
