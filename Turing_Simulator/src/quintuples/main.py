class Quintuple:
    def __init__(self,state,inp,output,prox,direction):
        self.state = state
        self.inp = inp
        self.output = output
        self.prox = prox
        self.direction = direction
 
    def _get_state(self):
        return self.state

    def _get_input(self):
        return self.inp

    def _get_prox(self):
        return self.prox

    def _get_output(self):
        return self.output

    def _get_direction(self):
        return self.direction