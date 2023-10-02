from enum import Enum

def get_size(size: str) -> 'Size':
    return Size(size)

class Size(Enum):
    """Available sizes in D&D 5e.
    """
    TINY = "T"
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"
    HUGE = "H"
    GARGANTUAN = "G"