from enum import Enum

def get_damage_type(damage_type: str) -> 'DamageType':
    damage_type = damage_type.lower()
    return DamageType(damage_type)

class DamageType(Enum):
    """Available damage types in D&D 5e.
    """
    ACID = "acid"
    BLUDGEONING = "bludgeoning"
    COLD = "cold"
    FIRE = "fire"
    FORCE = "force"
    LIGHTNING = "lightning"
    NECROTIC = "necrotic"
    PIERCING = "piercing"
    POISON = "poison"
    PSYCHIC = "psychic"
    RADIANT = "radiant"
    SLASHING = "slashing"
    THUNDER = "thunder"