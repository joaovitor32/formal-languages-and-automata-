class Cell:
    def __init__(self,previous,prox,value):
        self.prox = prox
        self.previous = previous
        self.value = value
    
    def get_value(self):
        return self.value

    def set_value(self,value):
        self.value = value

    def get_prox(self):
        return self.prox
    
    def set_prox(self,prox):
        self.prox =  prox
    
    def get_previous(self):
        return self.previous

    def set_previous(self,previous):
        self.previous = previous