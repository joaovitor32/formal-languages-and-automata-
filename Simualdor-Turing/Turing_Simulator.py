import pandas as pd
import inquirer

from Quintuples import Quintuple
from Tape import Tape
'''
https://pt.stackoverflow.com/questions/158043/o-que-%C3%A9-a-m%C3%A1quina-de-turing#:~:text=Uma%20m%C3%A1quina%20de%20Turing%20consiste,s%C3%ADmbolo%20de%20algum%20alfabeto%20finito.&text=Assume%2Dse%20que%20a%20fita,%C3%A9%20necess%C3%A1rio%20para%20a%20computa%C3%A7%C3%A3o.
'''
class Turing_Simulator:
    def __init__(self,quintuples):
        self.quintuples = [] 
        for row in quintuples.iterrows():
            quintuple = Quintuple(
                row[1]['state'],
                row[1]['input'],
                row[1]['output'],
                row[1]['next'],
                row[1]['direction'],
            )
            self.quintuples.append(quintuple)

    def get_state_object(self,inp,state):
        return [j for j in self.quintuples if (j.get_state() == state and j.get_input() == inp)][0]

    def show_tape(self):
        return 1

    #Function to give response after a tape is fullfiled
    def execute(self,initial_state,input_string):
        initial_blank, final_blank = Tape().start_tape(input_string)

        tape_cell = initial_blank.prox
        head = self.get_state_object(0,initial_state)
        list_str = list(map(int,input_string))

        for inp in list_str:
            tape_cell.value = head.get_output()
            
            if head.get_direction() == "R":
                tape_cell=tape_cell.get_prox()
            elif head.get_direction() == "L":
                tape_cell=tape_cell.get_previous()

            next_state = head.get_prox()
            head = self.get_state_object(inp,next_state)
            print(head.get_output())

    #Function to start application - get Initial State and Input string
    def start(self): 
        main=True
        options = [['Sim',True],['Não',False]]
        while main:
            try:
                question = [inquirer.List('prompt',message="Deseja continuar?",choices=[options[0][0],options[1][0]])]
                main = options[[i[0] for i in options].index(inquirer.prompt(question)['prompt'])][1]
                
                if not main:
                    break
        

                initial_state =  input('Initial state:')    
                input_string = input('Input string:')
                self.execute(initial_state,input_string)

            except KeyboardInterrupt:
                print("\n Algm erro aparentemente aconteceu")
                sys.exit(0)

if __name__=="__main__":    
    quintuples = pd.read_excel('Turing.ods', engine='odf') 
    Turing = Turing_Simulator(quintuples)
    Turing.start()
