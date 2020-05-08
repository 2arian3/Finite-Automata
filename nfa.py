# Arian Boukani 9731012
# nondeterministic finite automata class
class NFA :
    # alphabet is the list of the legal inputs
    # states is a list that contains the name of the possible states
    # final_states is a list because we might have a machine with more than one final state
    # vertices is the list of vertices that each component is a list with three components
    # the first one is the name of the starting state, the second component is the given input and the last one is the result state
    def __init__(self, alphabet, states, initial_state, final_states, vertices) :
        self.alphabet = alphabet
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.vertices = vertices
        if states[0] != initial_state :
            index = states.index(initial_state)
            self.states[0], self.states[index] = self.states[index], self.states[0]
        # i used nested dictionary structure to store the transition function with this format :
        # for example : {'q0' : {alpha0 : ['q1', 'q2'], alpha1 : ['q2'], ...}, 'q1' : {alpha1 : ['q2', 'q0, 'q3'], alpha2 : ['q3'] ...}, ...}
        # since in nfa a single input could result in different states, i used python built-in list to store the states
        # something that we didn't have in dfa    
        delta_func = dict()
        for state in states :
            delta_func[state] = dict()
        for vertex in vertices :
            if vertex[1] not in delta_func[vertex[0]] :
                if vertex[1] not in self.alphabet : vertex[1] = 'lambda'
                delta_func[vertex[0]][vertex[1]] = [vertex[2]]
            else : delta_func[vertex[0]][vertex[1]].append(vertex[2])   
        self.delta_func = delta_func
    # finding the lambda closure of the given state in the machine
    # result is a set of the states      
    def lambda_closure(self, state) :
        res = {state}
        for vertex in self.vertices :
            if vertex[0] in res and vertex[1] not in self.alphabet :
                res.add(vertex[2])
        return res      
