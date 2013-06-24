
from solver.norvig.search import * 
from solver.dictionaries import bigram

class WordChain(object):
    def __init__(self, words):
        entries = [[w, {'word': w, 'link': None, 'prev': None, 'next': None}] for w in words]
        self.chain = dict(entries)
        self.unlinked_before = set(words)
        self.unlinked_after = set(words)

    def link(self, a, link_word, b):
        # TODO: Confirm at least that b exists in the chain
        self.chain[a]['link'] = link_word 
        self.chain[a]['next'] = self.chain[b] 
        self.chain[b]['prev'] = self.chain[a]
        self.unlinked_before.remove(b)
        self.unlinked_after.remove(a)



class WordChainProblem(Problem):
    def __init__(self, initial, goal, dictionary):
        super(initial, goal)
        self.bigrams = dictionary

    def successor(self, state):
        return None

    
