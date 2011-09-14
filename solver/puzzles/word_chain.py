
from solver.norvig.search import * 
from solver.dictionaries import bigram

class WordChain(object):
    def __init__(self, words):
          self.words = words


class WordChainProblem(Problem):
    def __init__(self, initial, goal, dictionary):
        super(initial, goal)
        self.bigrams = dictionary

    def successor(self, state):
        return None

    
