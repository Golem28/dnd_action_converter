import nltk
from nltk.chunk import RegexpParser
import re

from .damage_type import get_grammatik_list as get_damage_type_grammatik
from .size import get_grammatik_list as get_size_grammatik
from .type import get_grammatik_list as get_monster_type_grammatik
from .condition import get_grammatik_list as get_condition_grammatik

patterns = [
        (r'(\d+)?d\d+', 'DICE'),                                # Dice pattern
        (r'\+\d+', 'ROLL_BONUS'),                                # Roll bonus pattern
        (r'\d+', 'NUMBER'),                                     # Number pattern
        (r'dc', 'DC'),                                           # DC pattern
        (re.compile(get_damage_type_grammatik()), 'DAM_TYPE'),  # Damage type pattern
        (re.compile(get_size_grammatik()), 'M_SIZE'),           # Size pattern
        (re.compile(get_monster_type_grammatik()), 'M_TYPE'),   # Type pattern
        (re.compile(get_condition_grammatik()), 'CONDITION'),   # Condition pattern
        (r'and|or', 'CONJ'),                                    # Conjunction pattern
        (r'damage' , 'DAMAGE'),                                 # Damage pattern
        (r'reach', 'REACH'),                                    # Reach pattern
        (r'ft', 'FEET'),                                           # Feet pattern
        (r'melee', 'MELEE'),                                    # Melee pattern
        (r'ranged', 'RANGED'),                                  # Ranged pattern
        (r'until', 'TIME_COND'),                                 # Time condition pattern
        (r'escape', 'ESCAPE'),                                  # Escape check pattern
        (r'hit', 'HIT'),                                        # Hit pattern
        {r'to', 'TO'},                                          # To pattern
        (r',', 'COMMA'),                                         # Comma pattern
        (r'\(|\{|\[', "("),                                        # Open bracket pattern
        (r'\)|\}|\]', ")"),                                        # Close bracket pattern
        (r'.*', 'X')                                           # other words
]

grammar = r"""
DAMAGE_PHRASE: {<NUMBER> <\(>* <X>* <DICE> <\)>* <DAM_TYPE> <DAMAGE>}
REACH_PHRASE: {<REACH> <NUMBER> <FEET>}
DC_PHRASE: {<DC> <NUMBER>}
HIT_PHRASE: {<\(>* <X>* <HIT> <ROLL_BONUS> <\)>* <TO> <HIT>}
"""
    

def interprete():
    regexp_tagger = nltk.RegexpTagger(patterns)
    # string = "melee weapon attack: {@hit +6} to hit, reach 5 ft., one target. hit: 18 ({@dice 4d6+4}) bludgeoning damage. and the target is grappled (escape dc 14). until this grapple ends, the target is restrained, user can automatically hit the target with its tail, and user can't make tail attacks against other targets."
    string = "melee attack: {@hit +5} to hit, reach 10 ft., one creature of size medium or smaller. hit: the target is grappled and restrained."
    words = nltk.word_tokenize(string)
    tagged_words = regexp_tagger.tag(words)
    print(tagged_words)
    
    chunk_parser = RegexpParser(grammar)
    tree = chunk_parser.parse(tagged_words)
    tree.draw()