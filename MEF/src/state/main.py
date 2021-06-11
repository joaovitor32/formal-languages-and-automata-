class State:
    def __init__(self,state,input0,input1,output):
        self.state = state
        self.output = output
        self.transitions = [input0,input1]

    def _get_state(self):
        return self.state
    
    def _get_transitions(self):
        return self.transitions
    
    def _get_output(self):
        return str(self.output)
