from enum import Enum


def get_condition(condition: str) -> 'Condition':
    condition = condition.lower()
    return Condition(condition)

def get_grammatik_list() -> str:
    gr_list = []
    for condition in Condition:
        gr_list.append(f"({condition.name.lower()})")
    return "|".join(gr_list)

class Condition(Enum):
    """Available conditions in D&D 5e.
    """
    CHARMED = "charmed"
    DEAFENED = "deafened"
    FRIGHTENED = "frightened"
    GRAPPLED = "grappled"
    INCAPACITATED = "incapacitated"
    INVISIBLE = "invisible"
    PARALYZED = "paralyzed"
    PETRIFIED = "petrified"
    POISONED = "poisoned"
    PRONE = "prone"
    RESTRAINED = "restrained"
    STUNNED = "stunned"
    UNCONCIOUS = "unconcious"