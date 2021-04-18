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

def transition_function(initialState,finalState,transitions):
    return
    
class Finite_State_Machine:
    def __init__(states,inputs,initialState,finalState,transition_function):
        self.transition_function = transition_function
        self.initialState = initialState
        self.finalState = finalState
        self.inputs = inputs
        self.states = states 

if __name__=="__main__":
    # Uma matriz nx3 que representa a descrição da tabela de estado de tal máquina
    machine = pd.read_excel('MEF.ods', engine='odf')
    print(machine)
