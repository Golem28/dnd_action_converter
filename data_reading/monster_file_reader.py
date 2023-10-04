from .monster import Monster
from typing import List

import json
import os

class MonsterFileReader:
    """A class that reads monster files and returns a list of Monster objects.
    """
    
    def __init__(self, folder_path: str) -> None:
        """Initializes the MonsterFileReader class.

        Args:
            folder_path (str): Path of the folder containing the monster files.
        """
        self._folder_path = folder_path

    def read_monsters(self) -> List[Monster]:
        """Reads all the monster files in the folder and returns a list of Monster objects.

        Returns:
            List[monster]: A list of Monster objects.
        """
        valid_monsters = []

        for filename in os.listdir(self._folder_path):
            if not filename.endswith(".json"):
                continue
            
            print(f"Processing {filename}...")
                
            file_path = os.path.join(self._folder_path, filename)
            
            with open(file_path, "r") as file:
                data: dict = json.load(file)
                monsters_list: list = data.get("monster", [])
                
                for monster_data in monsters_list:
                    monster = Monster(monster_data)
                    valid_monsters.append(monster)

            """try:
                
                        
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")"""

        return valid_monsters
