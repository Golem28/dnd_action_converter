from enum import Enum
from typing import Union

def get_type(type: Union[str, dict]) -> 'Type':
    if isinstance(type, dict):
        type = type.get('type', '')
    
    type = type.lower()
    return Type(type)

def get_grammatik_list() -> str:
    gr_list = []
    for type in Type:
        gr_list.append(f"({type.name.lower()})")
    return "|".join(gr_list)

class Type(Enum):
    """Available monster categories in D&D 5e.
    """
    FEY = "fey"
    HUMANOID = "humanoid"
    ABERRATION = "aberration"
    CELESTIAL = "celestial"
    CONSTRUCT = "construct"
    DRAGON = "dragon"
    FIEND = "fiend"
    ELEMENTAL = "elemental"
    GIANT = "giant"
    MONSTROSITY = "monstrosity"
    OOZE = "ooze"
    PLANT = "plant"
    UNDEAD = "undead"