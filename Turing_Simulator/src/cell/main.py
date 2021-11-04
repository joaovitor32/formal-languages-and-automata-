from __future__ import annotations


class Cell:
    def __init__(self, previous: Cell, prox: Cell, value: int) -> None:
        self.prox = prox
        self.previous = previous
        self.value = value

    def _get_value(self) -> int:
        return self.value

    def _set_value(self, value) -> None:
        self.value = value

    def _get_prox(self) -> Cell:
        return self.prox

    def _set_prox(self, prox: Cell) -> None:
        self.prox = prox

    def _get_previous(self) -> Cell:
        return self.previous

    def _set_previous(self, previous: Cell) -> None:
        self.previous = previous
