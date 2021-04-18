import pandas as pd
import inquirer

def acceptor(valids):
    ''' Acceptor style finite state machine for user input '''
    if not len(valids) is not 0:
        return 'Parece que chegamos ao estado final'
    else: 
        while True:
            questions = [inquirer.List('states',message="Qual será o próximo estado?",choices=[valids[0],valids[1]])]
            resp = inquirer.prompt(questions)
            return resp

def transition_function(initialState,finalState,transitions,output):
    outputString = ''
    resp = initial_state
    exit_state = finalState 

    while resp!=exit_state:
        response = transitions[transitions[:,0]==resp][0,1:]
        resp = acceptor(response)['states']
        outputString += str(output[output[:,0]==resp][0,1:][0])
    
    return outputString
    
class Finite_State_Machine:
    def __init__(self,states,initial_state,final_state,transition_function):
        self.transition_function = transition_function
        self.initial_state = initial_state
        self.final_state = final_state
        self.states = states 
    
    def execute(self):
        states = self.states.iloc[:,0].values
        transitions = self.states.iloc[:,0:3].values
        output = self.states.iloc[:,0:4:3].values
        response = self.transition_function(self.initial_state,self.final_state,transitions,output)
        print(response)


if __name__=="__main__":
    # Uma matriz nx3 que representa a descrição da tabela de estado de tal máquina
    states = pd.read_excel('MEF.ods', engine='odf')

    initial_state = input('Initial state:')
    exit_state = input('Exit State:')

    MEF = Finite_State_Machine(states,initial_state,exit_state,transition_function)
    MEF.execute()