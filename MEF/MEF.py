
import pandas as pd
import inquirer

class State:
    def __init__(self,state,input0,input1,output):
        self.state = state
        self.output = output
        self.transitions = [input0,input1]

class Finite_State_Machine:
    def __init__(self,states):
        self.states = [] 
        for row in states.iterrows():
            state = State(row[1]['estado'],[0,row[1][0]],[1,row[1][1]],row[1]['output'])
            self.states.append(state)

    def acceptor(self,valids,input_pop):
        if not len(valids) is not 0:
            return 'Parece que chegamos ao estado final'
        return str(list(valids)[int(input_pop)][1])

    def transition_function(self):

        outputString = ''
        str_array = list(self.input_string)
        resp = self.initial_state.state

        while len(str_array)>0:
            input_pop = str_array.pop(0)
            response =  self.states[[i.state for i in self.states].index(resp)]
            resp = self.acceptor(response.transitions,input_pop)
            outputString += str(response.output)
        
        return outputString
            
    def start(self): 
        main=True
        options = [['Sim',True],['Não',False]]
        while main:
            question = [inquirer.List('prompt',message="Deseja continuar?",choices=[options[0][0],options[1][0]])]
            main = options[[i[0] for i in options].index(inquirer.prompt(question)['prompt'])][1]
            
            if not main:
                break
    
            self.initial_state =  self.states[[i.state for i in self.states].index(input('Initial state:'))]    
            self.input_string = input('Input string:')
            self.execute()
    

    def execute(self):
        response = self.transition_function()
        print("Output: ",response)


if __name__=="__main__":    
    '''
    S: 
        States
        Alfa
        Outputs

    M: (S,input_string,alfa,initial_state,exit_state,transitions)
    M: (S,transitions)
    '''
    # Uma matriz nx3 que representa a descrição da tabela de estado de tal máquina
    states = pd.read_excel('MEF.ods', engine='odf')
    MEF = Finite_State_Machine(states)
    MEF.start() 