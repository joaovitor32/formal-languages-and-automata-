import pandas as pd

from state.main import State
from finite_state_machine.main import Finite_State_Machine

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

    states = pd.read_excel('./data/MEF.ods', engine='odf')
    MEF = Finite_State_Machine(State,states)
    MEF._start() 