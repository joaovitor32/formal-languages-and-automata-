from Cell import Cell

class Tape:
    def __init__(self):
        self.start = Cell(None,None,None)
        self.end = Cell(None,None,None)

    def start_tape(self,inputs):
        first_cell = Cell(None,self.start,inputs[0])
        end_cell = Cell(None,self.end,inputs[len(inputs)-1])

        self.start.prox = first_cell
        self.end.previous = end_cell

        current = first_cell.prox
        for inp in inputs[1:-1]:
            new_cell = Cell(None,current,inp)
            current.prox = new_cell
            new_cell.previous = current
            current = current.prox
            
        current.prox=self.end

        return [self.start,self.end]

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end