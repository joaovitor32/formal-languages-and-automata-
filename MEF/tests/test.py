
# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import sys
import pathlib

here = pathlib.Path(__file__).parents

sys.path.insert(1, '{}/src'.format(here[1]))

import unittest
import pandas as pd

from state.main import State
from finite_state_machine.main import  Finite_State_Machine

class TestSimple(unittest.TestCase):

    def test_format(self):
        states = pd.read_excel('./data/MEF.ods', engine='odf')
        mef = Finite_State_Machine(State,states)
        mef.initial_state = mef.states[[i.state for i in mef.states].index("s0")]    
        mef.input_string = "10001"
        output_string = mef.transition_function()
        self.assertEqual(output_string,"000000")
        pass 


if __name__ == '__main__':
    unittest.main()