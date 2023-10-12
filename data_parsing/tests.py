import nltk
from nltk import CFG
from nltk.parse.generate import generate

# Define the CFG for dice patterns
grammar = CFG.fromstring("""
    S -> DICE
    DICE -> NUMBER 'd' NUMBER | 'd' NUMBER
    NUMBER -> Z | Z Z | Z Z Z
    Z -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
""")

parser = nltk.ChartParser(grammar)

tree = parser.parse("10d60")
print(list(tree))
