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
    def check_existence(self,state):
        return [j for j in self.quintuples if (j.get_state() == state)]

    #Function to pick an quintuple from quintuples list
    def transition_function(self,inp,state):
        try:
            return [j for j in self.quintuples if (str(j.get_state()) == state and str(j.get_input()) == str(inp))][0]
        except ValueError:
            print("Estado não encontrado na lista de Quintuplas")


    #Function to show Tape
    def show_tape(self,initial,final):
        output = "Tape: Primeira Célula ->"
        while initial is not final:
            output+=str(initial.get_value())
            initial = initial.get_prox()
        print(output)

    #Function to give response after a tape is fullfiled
    #tape_cell.set_value does not work e tem algum erro 
    def execute(self,initial_state,input_string,stopping_criterion):
        i = 0

        initial_blank, final_blank = self.tape.start_tape(input_string)

        quintuples_route = []
        tape_cell = initial_blank.get_prox()
        current = tape_cell
    
        next_state = initial_state

        # None = blank, ou seja espaços brancos da memória
        while i < stopping_criterion: 
            
            inp = current.get_value()

            head = self.transition_function(inp,next_state)

            if current.get_prox() == final_blank:
                new_end_cell = self.tape.create_cell(current,final_blank,None)
                current.set_prox(new_end_cell)
                final_blank.set_previous(new_end_cell)
            
            if current.get_previous() == initial_blank and i != 0:
                new_start_cell =  self.tape.create_cell(initial_blank,current,None)
                current.set_previous(new_start_cell)
                initial_blank.set_previous(new_start_cell)

            current.set_value(head.get_output())

            if head.get_direction() == "R":              
                current = current.get_prox()
            elif head.get_direction() == "L":
                current = current.get_previous()

            next_state = head.get_prox()

            i=i+1

        self.show_tape(tape_cell,final_blank.get_previous())

    #Function to start application - get Initial State and Input string
    def start(self): 
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
                self.execute(initial_state,input_string,stopping_criterion)

            except KeyboardInterrupt:
                print("\n Algm erro aparentemente aconteceu")
                sys.exit(0)
