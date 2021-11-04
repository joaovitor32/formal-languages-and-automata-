class Quintuple:
    def __init__(self, state: str, inp: int, output: int, prox: str, direction: str) -> None:
        self.state = state
        self.inp = inp
        self.output = output
        self.prox = prox
        self.direction = direction

    def _get_state(self) -> str:
        return self.state

    def _get_input(self) -> int:
        return self.inp

    def _get_prox(self) -> str:
        return self.prox

    def _get_output(self) -> int:
        return self.output

    def _get_direction(self) -> str:
        return self.direction
