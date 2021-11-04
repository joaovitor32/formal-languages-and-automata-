class State:
    def __init__(self, state: str, input0: int, input1: int, output: int) -> None:
        self.state = state
        self.output = output
        self.transitions = [input0, input1]

    def _get_state(self) -> str:
        return self.state

    def _get_transitions(self) -> list[float]:
        return self.transitions

    def _get_output(self) -> float:
        return str(self.output)
