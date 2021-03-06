import inquirer
import sys

import pandas as pd

from quintuples.main import Quintuple
from tape.main import Tape
from cell.main import Cell


class Turing_Simulator:
    def __init__(self, Quintuple: Quintuple, Tape: Tape, Cell: Cell, quintuples: pd.DataFrame) -> None:
        self.quintuples = []
        self.tape = Tape(Cell)
        for row in quintuples.iterrows():
            self.quintuples.append(Quintuple(
                row[1]['state'],
                row[1]['input'],
                row[1]['output'],
                row[1]['next'],
                row[1]['direction'],
            ))

    """
        Function to check if state exists
    """

    def _check_existence(self, state: str) -> list[Quintuple]:
        return [j for j in self.quintuples if (j._get_state() == state)]

    """
        Function to pick an quintuple from quintuples list
    """

    def _transition_function(self, inp: str, state: str) -> list[Quintuple]:
        try:
            return [j for j in self.quintuples if (j._get_state() == state and str(j._get_input()) == str(inp))][0]
        except ValueError:
            print("\nString não pode ser interpretada por está máquina... halt")
            sys.exit(1)

    """
        Function to show Tape
    """

    def _show_tape(self, initial: Quintuple, final: Quintuple):
        output = "Tape: Primeira Célula ->"
        while initial is not final:
            output += str(initial._get_value())
            initial = initial._get_prox()
        print(output)

    """
        Set new direction to move in the tape
    """

    def _update_direction(self, current: Cell, head: Quintuple) -> Cell:
        if head._get_direction() == "R":
            current = current._get_prox()
        elif head._get_direction() == "L":
            current = current._get_previous()

        return current

    """
       Update the beginning of the tape
    """

    def _update_final_blank(self, final_blank: Cell, current: Cell) -> None:
        new_end_cell = self.tape._create_cell(
            current, final_blank, None)
        current._set_prox(new_end_cell)
        final_blank._set_previous(new_end_cell)

    def _update_initial_blank(self, initial_blank: Cell, current: Cell) -> None:
        new_start_cell = self.tape._create_cell(
            initial_blank, current, None)
        current._set_previous(new_start_cell)
        initial_blank._set_previous(new_start_cell)

    """
        Function to give response after a tape is fullfiled
    """

    def _execute(self, initial_state: str, input_string: str, stopping_criterion: int) -> None:
        counter = 0

        initial_blank, final_blank = self.tape._start_tape(input_string)

        tape_cell = initial_blank._get_prox()
        current = tape_cell

        next_state = initial_state

        """
            None = blank, ou seja espaços brancos da memória
        """
        while counter < stopping_criterion:

            inp = current._get_value()

            head = self._transition_function(inp, next_state)

            if current._get_prox() == final_blank:
                self._update_final_blank(final_blank, current)

            if current._get_previous() == initial_blank and counter != 0:
                self._update_initial_blank(initial_blank, current)

            current._set_value(head._get_output())

            current = self._update_direction(current, head)
            next_state = head._get_prox()

            counter = counter + 1

        self._show_tape(tape_cell, final_blank._get_previous())

    """
        Function to start application - get Initial State and Input string
    """

    def _start(self) -> None:
        main = True
        options = [['Sim', True], ['Não', False]]
        stopping_criterion = 0
        while main:
            try:
                question = [inquirer.List('prompt', message="Deseja continuar?", choices=[
                    options[0][0], options[1][0]])]
                main = options[[i[0] for i in options].index(
                    inquirer.prompt(question)['prompt'])][1]

                if not main:
                    break

                stopping_criterion = int(input("Insira o critério de parada:"))
                initial_state = input('Initial state:')
                input_string = input('Input string:')
                self._execute(initial_state, input_string, stopping_criterion)

            except KeyboardInterrupt:
                print("\n Algm erro aparentemente aconteceu")
                sys.exit(0)
