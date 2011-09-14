from solver.puzzles.word_chain import * 

class TestWordChain:
    def setup_method(self, method):
        self.words = ["racer", "wing", "child"]
        self.chain = WordChain(self.words)
        
    def test_unlinked_at_start(self):
        assert self.chain.unlinked_before == set(self.words)
        assert self.chain.unlinked_after == set(self.words)

    def test_link(self):
        self.chain.link("racer", "x", "wing")

    def test_unlinked_after_link(self):
        self.chain.link("racer", "x", "wing")
        assert "wing" not in self.chain.unlinked_before
        assert "racer" not in self.chain.unlinked_after

