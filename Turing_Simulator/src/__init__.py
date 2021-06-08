
import pandas as pd
from turing_machine.main import Turing_Simulator
from quintuples.main import Quintuple
from tape.main import Tape
from cell.main import Cell
'''
https://pt.stackoverflow.com/questions/158043/o-que-%C3%A9-a-m%C3%A1quina-de-turing#:~:text=Uma%20m%C3%A1quina%20de%20Turing%20consiste,s%C3%ADmbolo%20de%20algum%20alfabeto%20finito.&text=Assume%2Dse%20que%20a%20fita,%C3%A9%20necess%C3%A1rio%20para%20a%20computa%C3%A7%C3%A3o.
'''

# Testar questão 11 página 781
if __name__=="__main__":    
    quintuples = pd.read_excel('./data/Turing.ods', engine='odf') 
    Turing = Turing_Simulator(Quintuple,Tape,Cell,quintuples)
    Turing.start()