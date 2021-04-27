class Cell:
    def __init__(self,previous,prox,value):
        self.prox = prox
        self.previous = previous
        self.value = value
    
    def get_value(self):
        return self.value

    def get_prox(self):
        return self.prox
    
    def get_previous(self):
        return self.previous