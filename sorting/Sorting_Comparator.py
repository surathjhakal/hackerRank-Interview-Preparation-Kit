class Player:
    def __init__(self, name, score):
        self.name=name
        self.score=score
        
    def comparator(self, b):
        if self.score==b.score:
            return 1 if self.name>b.name else -1
        
        return b.score-self.score
