
import pandas as pd
import inquirer

class State:
    def __init__(self,state,input0,input1,output):
        self.state = state
        self.output = output
        self.transitions = [input0,input1]

    def get_state(self):
        return self.state
    
    def get_transitions(self):
        return self.transitions
    
    def get_output(self):
        return str(self.output)

class Finite_State_Machine:
    #Creating objects State array 
    def __init__(self,states):
        self.states = [] 
        for row in states.iterrows():
            state = State(row[1]['estado'],[0,row[1][0]],[1,row[1][1]],row[1]['output'])
            self.states.append(state)

    #Function to determine the next state based on input
    def acceptor(self,valids,input_pop):
        if not len(valids) !=0:
            return 'Parece que chegamos ao estado final'
        return self.states[[j.get_state() for j in self.states].index(str(list(valids)[int(input_pop)][1]))]

    #Function that follows the trajectory related to states and inputs
    def transition_function(self):

        outputString = ''
        str_array = list(self.input_string)
        resp = self.initial_state

        '''
            Every iteration the first input of array is 
            picked and an analysis is made to determine
            which one is the next state based on the
            transitions array prop of every State object.
        '''

        outputString += self.states[self.states.index(resp)].get_output()
        while len(str_array) != 0:
            input_pop = str_array.pop(0)
            response =  self.states[self.states.index(resp)]
            resp = self.acceptor(response.get_transitions(),input_pop)
            outputString += response.get_output()
        
        return outputString
            
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

        
                print("Estados existentes:",[i.state for i in self.states])
                self.initial_state =  self.states[[i.state for i in self.states].index(input('Initial state:'))]    
                self.input_string = input('Input string:')
                self.execute()

            except KeyboardInterrupt:
                print("\n Algum erro aparentemente aconteceu")
                sys.exit(0)
    
    #Function to give response after a trajectory is made
    def execute(self):
        response = self.transition_function()
        print("Output: ",response)


if __name__=="__main__":    
    '''
    S: 
        States
        Alfa
        Outputs

    Theoretically
        M: (S,input_string,alfa,initial_state,exit_state,transitions)
    '''
    # Uma matriz nx3 que representa a descrição da tabela de estado de tal máquina
    """
    State |    Previous(0)  (1)  | Output
    ---------------------------------------
        s0      |   s0      s1  |   0
        s1      |   s1      s2  |   0
        s2      |   s2      s3  |   0
        s3      |   s3      s4  |   0
        s4      |   s1      s4  |   1
    """

    states = pd.read_excel('MEF.ods', engine='odf')
    MEF = Finite_State_Machine(states)
    MEF.start() 