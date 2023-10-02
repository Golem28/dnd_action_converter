from .size import Size, get_size
from .type import Type, get_type


class Monster:
    """A class that represents a monster in D&D 5e.
    """

    def __init__(self, monster: dict):
        """Initializes the Monster class.

        Args:
            monster (dict): A dictionary containing the monster data.
        """
        self._monster = monster
        print(f"Monster created: {self.get_name()}")

    def get_name(self) -> str:
        return self._monster["name"]
    
    def get_source(self) -> str:
        return self._monster["source"]

    def get_size(self) -> Size:
        size = get_size(self._monster["size"])
        return size

    def get_type(self) -> Type:
        type = get_type(self._monster["type"])
        return type

    def get_alignment(self) -> dict:
        return self._monster["alignment"]
    
    def get_armor_class(self) -> str:
        return self._monster["ac"]
    
    def get_hit_points(self) -> int:
        return self._monster["hp"]["average"]
    
    def get_speeds(self) -> dict:
        return self._monster["speed"]
    
    def get_strength(self) -> int:
        return self._monster["str"] 
    
    def get_dexterity(self) -> int:
        return self._monster["dex"]
    
    def get_constitution(self) -> int:
        return self._monster["con"]
    
    def get_intelligence(self) -> int:
        return self._monster["int"]
    
    def get_wisdom(self) -> int:
        return self._monster["wis"]
    
    def get_charisma(self) -> int:
        return self._monster["cha"]

    def get_saving_throws(self) -> dict:
        return self._monster["save"]
    
    def get_skills(self) -> dict:
        return self._monster["skill"]
    
    def get_passive_perception(self) -> int:
        return self._monster["passive"]
    
    def get_actions(self) -> list:
        return self._monster.get("action", [])
    
    def get_traits(self) -> list:
        return self._monster.get("trait", [])
    
    def get_page(self) -> str:
        return self._monster["page"]