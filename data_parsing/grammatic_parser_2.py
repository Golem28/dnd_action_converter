import nltk

# action = "The oni magically polymorphs into a Small or Medium humanoid, into a Large giant, or back into its true form. Other than its size, its statistics are the same in each form. The only equipment that is transformed is its glaive, which shrinks so that it can be wielded in humanoid form. If the oni dies, it reverts to its true form, and its glaive reverts to its normal size."
# action = "The dragon exhales a flashing mote of radiant energy that travels to a point the dragon can see within 240 feet of itself, then blossoms into a 40-foot-radius sphere centered on that point. Each creature in the sphere must make a DC 23 Constitution saving throw, taking 66 (12d10) radiant damage on a failed save, or half as much damage on a successful one."
# action = "Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 21 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours."
# action = "The dragon exhales an icy blast in a 90-foot cone. Each creature in that area must make a DC 22 Constitution saving throw, taking 72 (16d8) cold damage on a failed save, or half as much damage on a successful one."
# action = "if the target is a Large or smaller creature, the target must succeed on a DC 18 Strength saving throw or be trapped in the anhkolox's rib cage and grappled (escape DC 18). Until this grapple ends, the target is restrained, and the anhkolox can't use Entrapping Rend on another target."
# action = "While the assassin vine remains motionless, it is indistinguishable from a normal plant."
action = """Drifting through the dark waters of the Netherdeep, the death embrace is an ominous sight. Beneath its bell hangs a lacy, tendrilous mass that thrums with magic, surrounded by six 60-foot-long, barbed tentacles. The death embrace uses these tentacles to grasp and petrify its prey.

Despite its foreboding name, the death embrace is not an overly aggressive creature. It prefers to bide its time, using creatures it has caught in its tentacles as shields to absorb attacks."""

grammar = r"""
    NOUN: {<VBG>? <NN> | <NNS> | <NNP> | <NNPS> | <CD> (<\(> <CD> <\)>) | <CD> | <PRP>}
    VERB: {<MD>? <RB>* <VB>? <VBN> | <MD>? <RB>* <VB> |<MD>? <RB>* <VBD> | <MD>? <RB>* <VBP> | <MD>? <RB>* <VBZ> | <MD>? <RB>* <VBG>}
    ADJ: {<JJ> | <JJR> | <JJS>}
    MULTI_ADJ: {(<ADJ> <CC> <ADJ>)+ | <ADJ>+}
    SPEC: {<DT> | <PRP\$>}
    
    NP: {<SPEC>? <MULTI_ADJ>* <NOUN> (<POS>? <MULTI_ADJ>* <NOUN>)*}
    PP: {<RB>? (<IN> | <TO>) <NP>}
    PP: {<PP> (<,> <PP>)* (<,>? <CC> <PP>)*}
    VP: {<VERB> <NP> | <VERB> <PP>+ | <VERB> <NP> <PP>+ | <VERB> <MULTI_ADJ>}
    
    
    SENT: {<NP>* <PP>* <VP> <PP>*}
    SPEC_SENT: {<WDT> <SENT>}
    SENT: {<SENT> <SENT>+}
    SENT: {<SENT>+ <CC> <SENT>}
    SENT: {<SENT> <,> <SENT>}
    OR_PHRASE: {<CC> <NP> <PP> <PP>}
"""

def interprete_sentence(sentence: str):
    tagged_words = nltk.pos_tag(nltk.word_tokenize(sentence))
    chunk_parser = nltk.RegexpParser(grammar)
    tree = chunk_parser.parse(tagged_words)

    tree.draw()

    # Print each word of ACTORs
    for subtree in tree.subtrees():
        if subtree.label() == "SENTENCE_PART":
            # Print words without the tags
            print(" ".join([word[0] for word in subtree.leaves()]))

action = action.lower()

# Tag the words
sentences = nltk.sent_tokenize(action)

for sentence in sentences:
    interprete_sentence(sentence)