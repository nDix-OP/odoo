from enum import Enum


class DataType(Enum):
    ESTRUCTURADOS = 'Estructurados'
    SEMIESTRUCTURADOS = 'Semiestructurados'
    NO_ESTRUCTURADOS = 'No estructurados'

    # Other ver si se pasa como str o CategoryType, así funciona en ambos casos
    # Redefinir en cada Enum
    def __eq__(self, other):
        if isinstance(other, str):
            return str(self.name) == str(other)
        if isinstance(other, DataType):
            return other == self
        return False
