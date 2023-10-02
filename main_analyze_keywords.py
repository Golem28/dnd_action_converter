from data_reading import MonsterFileReader, Monster
from analyze_tools import ActionAnalyzer

import pathlib


if __name__ == '__main__':
    """Main method for getting the most common words in the action descriptions.
    """
    path = str(pathlib.Path(__file__).parent.absolute().joinpath("data"))
    file_reader = MonsterFileReader(path)
    monsters = file_reader.read_monsters()
    all_actions = [action for monster in monsters for action in monster.get_actions()]
    action_analyzer = ActionAnalyzer(all_actions)
    action_analyzer.get_often_used_words()