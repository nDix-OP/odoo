from enum import Enum


class Status(Enum):
    PROPUESTO = 'Propuesto'
    VIGENTE = 'Vigente'
    RETIRADO = 'Retirado'

    # Other ver si se pasa como str o CategoryType, así funciona en ambos casos
    # Redefinir en cada Enum
    def __eq__(self, other):
        if isinstance(other, str):
            return str(self.name) == str(other)
        if isinstance(other, Status):
            return other == self
        return False
