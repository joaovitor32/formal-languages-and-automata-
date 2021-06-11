import inquirer

class Turing_Simulator:
    def __init__(self,Quintuple,Tape,Cell,quintuples):
        self.quintuples = [] 
        self.tape = Tape(Cell)
        for row in quintuples.iterrows():
            quintuple = Quintuple(
                row[1]['state'],
                row[1]['input'],
                row[1]['output'],
                row[1]['next'],
                row[1]['direction'],
            )
            self.quintuples.append(quintuple)

    #Function to check if state exists
    def _check_existence(self,state):
        return [j for j in self.quintuples if (j._get_state() == state)]

    #Function to pick an quintuple from quintuples list
    def _transition_function(self,inp,state):
        try:
            return [j for j in self.quintuples if (str(j._get_state()) == state and str(j._get_input()) == str(inp))][0]
        except ValueError:
            print("Estado não encontrado na lista de Quintuplas")


    #Function to show Tape
    def _show_tape(self,initial,final):
        output = "Tape: Primeira Célula ->"
        while initial is not final:
            output+=str(initial._get_value())
            initial = initial._get_prox()
        print(output)

    #Function to give response after a tape is fullfiled
    #tape_cell.set_value does not work e tem algum erro 
    def _execute(self,initial_state,input_string,stopping_criterion):
        counter = 0

        initial_blank, final_blank = self.tape._start_tape(input_string)

        quintuples_route = []
        tape_cell = initial_blank._get_prox()
        current = tape_cell
    
        next_state = initial_state

        # None = blank, ou seja espaços brancos da memória
        while counter < stopping_criterion: 
            
            inp = current._get_value()

            head = self._transition_function(inp,next_state)

            if current._get_prox() == final_blank:
                new_end_cell = self.tape._create_cell(current,final_blank,None)
                current._set_prox(new_end_cell)
                final_blank._set_previous(new_end_cell)
            
            if current._get_previous() == initial_blank and counter != 0:
                new_start_cell =  self.tape._create_cell(initial_blank,current,None)
                current._set_previous(new_start_cell)
                initial_blank._set_previous(new_start_cell)

            current._set_value(head._get_output())

            if head._get_direction() == "R":              
                current = current._get_prox()
            elif head._get_direction() == "L":
                current = current._get_previous()

            next_state = head._get_prox()

            counter = counter + 1

        self._show_tape(tape_cell,final_blank._get_previous())

    #Function to start application - get Initial State and Input string
    def _start(self): 
        main=True
        options = [['Sim',True],['Não',False]]
        stopping_criterion = 0
        while main:
            try:
                question = [inquirer.List('prompt',message="Deseja continuar?",choices=[options[0][0],options[1][0]])]
                main = options[[i[0] for i in options].index(inquirer.prompt(question)['prompt'])][1]
                stopping_criterion = int(input("Insira o critério de parada:"))

                if not main:
                    break
        
                initial_state =  input('Initial state:')    
                input_string = input('Input string:')
                self._execute(initial_state,input_string,stopping_criterion)

            except KeyboardInterrupt:
                print("\n Algm erro aparentemente aconteceu")
                sys.exit(0)
