import nltk
from nltk.stem import WordNetLemmatizer
from collections import Counter
import random
from typing import List
from nltk.parse import DependencyGraph

class ActionAnalyzer:
    
    def __init__(self, action_list: list) -> None:
        """Initializes the ActionAnalyzer class.

        Args:
            action_list (list): A list of dictionaries containing the actions of a monster and the name.
        """
        self._action_list = action_list
        # Load the nltk data
        nltk.download('stopwords')
        nltk.download('punkt')
        nltk.download('wordnet')
        nltk.download('averaged_perceptron_tagger')
        nltk.download("words")
        
    def get_action_descriptions(self) -> List[str]:
        """Tries to append each action description to a list of strings.
        
        TODO: Fix the method for actions containing lists or tables.

        Returns:
            List[str]: A list of strings containing the descriptions of the actions.
        """
        descriptions = []
        for action in self._action_list:
            try:
                desc = " ".join(action["entries"])
                descriptions.append(desc)
            except TypeError:
                print(f"Parsing Error: {action}")
                
        return descriptions
        
    def get_often_used_words(self, count: int = 100) -> None:
        """Prints the most common words in the action descriptions.
        For that it splits the words, lemmanizes them, removes unnecessary words and counts them.
        """
        descriptions = self.get_action_descriptions()
        words = nltk.word_tokenize(" ".join(descriptions).lower())
        lemmatizer = WordNetLemmatizer()
        words = [lemmatizer.lemmatize(word) for word in words]
        stop_words = set(nltk.corpus.stopwords.words("english"))
        words = [word for word in words if word not in stop_words]
        freq_words = nltk.FreqDist(words)
        print(freq_words.most_common(count))
        
    def get_random_action(self) -> dict:
        """Returns a random action from the action list.

        Returns:
            dict: A dictionary containing the name and description of a random action.
        """
        return self._action_list[random.randint(0, len(self._action_list) - 1)]
    
    def print_test_nltk_prework(self) -> None:
        """Prints the results of the nltk prework with a random action.
        """
        descriptions = "\n".join(self.get_random_action()["entries"]).lower()
        print(descriptions)
        lotr_pos_tags = nltk.pos_tag(nltk.word_tokenize(descriptions))
        print(lotr_pos_tags)
        # grammar = "NP: {<DT>?<JJ>*<NN>}"
        # chunk_parser = nltk.RegexpParser(grammar)
        #tree = chunk_parser.parse(lotr_pos_tags)
        #tree.draw()
        