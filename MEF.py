import pandas as pd
import inquirer

def Acceptor(valids):
    ''' Acceptor style finite state machine for user input '''
    if not len(valids) is not 0:
        return 'Parece que chegamos ao estado final'
    else: 
        while True:
            questions = [inquirer.List('states',message="Qual será o próximo estado?",choices=[valids[0],valids[1]])]
            resp = inquirer.prompt(questions)
            return resp

def finite_state_machine():
    outputString=''

    # Uma matriz nx3 que representa a descrição da tabela de estado de tal máquina
    MEF=pd.read_excel('MEF.ods', engine='odf')
    
    initial_state = input('Initial state:')
    exit_state = input('Exit State:')

    states=MEF.iloc[:,0].values
    transitions=MEF.iloc[:,0:3].values
    output=MEF.iloc[:,0:4:3].values

    resp=initial_state

    while resp!=exit_state:
        response = transitions[transitions[:,0]==resp][0,1:]
        resp=Acceptor(response)['states']
        outputString+=str(output[output[:,0]==resp][0,1:][0])

    print("A string de saída é: ",outputString)

if __name__=="__main__":
    finite_state_machine()
