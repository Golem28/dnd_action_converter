from enum import Enum

def get_size(size: str) -> 'Size':
    return Size(size)

def get_grammatik_list() -> str:
    gr_list = []
    for size in Size:
        gr_list.append(f"({size.name.lower()})")
    return "|".join(gr_list)

class Size(Enum):
    """Available sizes in D&D 5e.
    """
    TINY = "T"
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"
    HUGE = "H"
    GARGANTUAN = "G"