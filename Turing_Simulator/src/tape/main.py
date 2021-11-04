from cell.main import Cell


class Tape:
    def __init__(self, Cell: Cell) -> None:
        self.start = Cell(None, None, None)
        self.end = Cell(None, None, None)
        self.cell = Cell

    def _start_tape(self, inputs) -> list[Cell, Cell]:
        first_cell = self.cell(self.start, None, inputs[0])
        end_cell = self.cell(None, self.end, inputs[len(inputs)-1])

        self.start._set_prox(first_cell)
        self.end._set_previous(end_cell)

        current = first_cell
        for inp in inputs[1:-1]:
            new_cell = self.cell(current, None, inp)
            current._set_prox(new_cell)
            current = current._get_prox()

        current._set_prox(end_cell)
        end_cell._set_previous(current)

        return [self.start, self.end]

    def _get_start(self) -> Cell:
        return self.start

    def _get_end(self) -> Cell:
        return self.end

    def _create_cell(self, previous: Cell, prox: Cell, value: int) -> Cell:
        return self.cell(previous, prox, value)
