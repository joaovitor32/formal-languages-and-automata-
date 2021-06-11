class Cell:
    def __init__(self,previous,prox,value):
        self.prox = prox
        self.previous = previous
        self.value = value
    
    def _get_value(self):
        return self.value

    def _set_value(self,value):
        self.value = value

    def _get_prox(self):
        return self.prox
    
    def _set_prox(self,prox):
        self.prox =  prox
    
    def _get_previous(self):
        return self.previous

    def _set_previous(self,previous):
        self.previous = previous