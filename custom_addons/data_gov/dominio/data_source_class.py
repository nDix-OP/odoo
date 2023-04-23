from enum import Enum


class DataSourceClass(Enum):
    SERVIDOR_BD = 1
    SISTEMA_FICHEROS = 2
    API = 3
    SERVICIO_STREAMING = 4
    SISTEMA_TRANSFERENCIA_FICHEROS = 5
