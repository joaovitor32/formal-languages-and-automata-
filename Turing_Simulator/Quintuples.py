class Quintuple:
    def __init__(self,state,inp,output,prox,direction):
        self.state = state
        self.inp = inp
        self.output = output
        self.prox = prox
        self.direction = direction
 
    def get_state(self):
        return self.state

    def get_input(self):
        return self.inp

    def get_prox(self):
        return self.prox

    def get_output(self):
        return self.output

    def get_direction(self):
        return self.direction