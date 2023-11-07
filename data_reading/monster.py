from data_parsing import get_size, get_type, Size, Type
from typing import List
from nltk import word_tokenize


class Monster:
    """A class that represents a monster in D&D 5e.
    """

    def __init__(self, monster: dict):
        """Initializes the Monster class.

        Args:
            monster (dict): A dictionary containing the monster data.
        """
        self._monster = monster
        self._remove_dicts_from_actions()
        self._remove_monstername_from_actions()
        
    def _remove_dicts_from_actions(self) -> None:
        """Removes lists from the actions.
        """
        for action in self.get_actions():
            for index, entry in enumerate(action["entries"]):
                if isinstance(entry, dict):
                    entry = self._convert_action_dicts_to_string(entry)
                    action["entries"][index] = entry
                    
                    
    def _convert_action_dicts_to_string(self, action) -> str:
        """Converts the action dictionaries to strings.

        Args:
            action (dict): The action to be converted.

        Returns:
            str: The converted action.
        """
        string_action: str = ""
        
        if action["type"] == "list":            
            for subaction in action["items"]:
                if isinstance(subaction, str):
                    description = subaction
                elif isinstance(subaction, dict):
                    description = f"• [{subaction['name']}] {subaction['entry']}"
                else:
                    raise TypeError(f"Substructure type {type(subaction)} not supported.")
                
                string_action += description + "\n"
        elif action["type"] == "table":
            for labels in action["colLabels"]:
                string_action += f"{labels}\t"
            
            string_action += "\n"
            
            for row in action["rows"]:
                for entry in row:
                    string_action += f"{entry}\t"
                string_action += "\n"
        else:
            raise TypeError(f"Structure type {action['type']} not supported.")
        
        return string_action 
        
    def _remove_monstername_from_actions(self) -> None:
        """Removes the monster name from the actions.
        """
        namelist = word_tokenize(self.get_name())
        
        for action in self.get_actions():
            for index, entry in enumerate(action["entries"]):
                entry = self._replace_name_searchpattern(namelist, entry)
                action["entries"][index] = entry
                    
    def _replace_name_searchpattern(self, wordlist: List[str], sentence: str, replacement: str = "user") -> str:
        """Replaces the shortnames in the sentence with the replacement.

        Args:
            wordlist (List[str]): List of the possible shortnames to be replace.
            sentence (str): The sentence to be searched.
            replacement (str, optional): The word for the new action user's name. Defaults to "user".

        Returns:
            str: The sentence with the shortnames replaced as the replacement.
        """
        sentence = sentence.lower()
        
        for word in wordlist:
            word = word.lower()

            if f"the {word}" in sentence:
                sentence = sentence.replace(f"the {word}", replacement)
            elif sentence.startswith(word):
                sentence = sentence.replace(word, replacement, 1)
            elif sentence.startswith(f"a {word}"):
                sentence = sentence.replace(f"a {word}", replacement, 1)
        
        return sentence

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