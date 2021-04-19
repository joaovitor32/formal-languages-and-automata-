import pandas as pd
import inquirer

def acceptor(valids,input_pop):
    ''' Acceptor style finite state machine for user input '''
    if not len(valids) is not 0:
        return 'Parece que chegamos ao estado final'
    return str(list(valids)[int(input_pop)])

def transition_function(initial_state,input_string,transitions,output):
    outputString = ''
    resp = initial_state

    str_array = list(input_string)

    #while  resp!=exit_state
    while len(str_array)>0:
        input_pop = str_array.pop(0)
        response = transitions[transitions[:,0]==resp][0,1:]
        resp = acceptor(response,input_pop)
        outputString += str(output[output[:,0]==resp][0,1:][0])
    
    return outputString
    
class Finite_State_Machine:
    def __init__(self,states,transition_function):
        self.states = states 
        self.transition_function = transition_function

    def start(self): 
        main=True
        options = [['Sim',True],['Não',False]]
        while main:
            question = [inquirer.List('prompt',message="Deseja continuar?",choices=[options[0][0],options[1][0]])]
            main = options[[i[0] for i in options].index(inquirer.prompt(question)['prompt'])][1]
            
            if not main:
                break
            
            self.initial_state = input('Initial state:')
            self.input_string = input('Input string:')
            self.execute()
    
    def execute(self):
        states = self.states.iloc[:,0].values
        transitions = self.states.iloc[:,0:3].values
        output = self.states.iloc[:,0:4:3].values
        response = self.transition_function(self.initial_state,self.input_string,transitions,output)
        print("Output: ",response)


if __name__=="__main__":    
    # Uma matriz nx3 que representa a descrição da tabela de estado de tal máquina
    states = pd.read_excel('MEF.ods', engine='odf')
    #M: (S,input_string,alfa,initial_state,exit_state,transitions)
    MEF = Finite_State_Machine(states,transition_function)
    MEF.start()    