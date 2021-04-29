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
                int(row[1]['input']),
                int(row[1]['output']),
                row[1]['next'],
                row[1]['direction'],
            )
            self.quintuples.append(quintuple)

    #Function to pick an quintuple from quintuples list
    def get_state_object(self,inp,state):
        return [j for j in self.quintuples if (j.get_state() == state and j.get_input() == inp)][0]

    #Function to show Tape
    def show_tape(self,initial,final):
        while initial is not final:
            print(initial.get_value())
            initial = initial.get_prox()

    #Function to give response after a tape is fullfiled
    #tape_cell.set_value does not work e tem algum erro 
    def execute(self,initial_state,input_string):
        initial_blank, final_blank = Tape().start_tape(input_string)

        tape_cell = initial_blank.get_prox()
        current = tape_cell
    
        next_state = initial_state
        while ((current is not final_blank) and (initial_blank is not current)): 
            
            inp = current.get_value()
            head = self.get_state_object(inp,next_state)
            
            current.set_value(head.get_output())

            if head.get_direction() == "R":
                current = current.get_prox()
            elif head.get_direction() == "L":
                current = current.get_previous()
        
            
            if current.get_prox() == final_blank:    
                last_state = self.get_state_object(head.get_output(),head.get_state()).get_prox()
                new_end_value = self.get_state_object(head.get_output(),last_state).get_output()

                new_end_cell = Tape().create_cell(current,final_blank,None)
                current.set_prox(new_end_cell)
                final_blank.set_previous(new_end_cell)
                current = current.get_prox()
                current.set_value(new_end_value)
                break                
        
            if current.get_previous() == initial_blank:
                last_state = self.get_state_object(head.get_output(),head.get_state()).get_prox()
                new_start_value = self.get_state_object(head.get_output(),last_state).get_output()

                new_start_cell = Tape().create_cell(initial_blank,current,None)
                current.set_previous(new_start_cell)
                initial_blank.set_previous(new_start_cell)
                current = current.get_previous()
                current.set_value(new_start_value)
                break

            next_state = head.get_prox()

        self.show_tape(tape_cell,final_blank)

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
