
from Cell import Cell

class Tape:
    def __init__(self):
        self.start = Cell(None,None,None)
        self.end = Cell(None,None,None)

    def start_tape(self,inputs):
        first_cell = Cell(self.start,None,inputs[0])
        end_cell = Cell(None,self.end,inputs[len(inputs)-1])

        self.start.set_prox(first_cell)
        self.end.set_previous(end_cell)

        current = first_cell
        for inp in inputs[1:-1]:
            new_cell = Cell(current,None,inp)
            current.set_prox(new_cell)
            current = current.prox
        
        current.set_prox(end_cell)
        end_cell.set_previous(current)
        
        return [self.start,self.end]

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end
    
    def create_cell(self,previous,prox,value):
        return Cell(previous,prox,value)