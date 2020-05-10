# Arian Boukani 9731012
# deterministic finite automata class
class DFA :
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
        # i used nested dictionary structure to store the transition function with this format :
        # for example : {'q0' : {alpha0 : 'q1', alpha1 : 'q2', ...}, 'q1' : {alpha1 : 'q2', alpha2 : 'q3' ...}, ...}
        delta_func = dict()
        for state in states :
            delta_func[state] = dict()
        for vertex in vertices :
            delta_func[vertex[0]][vertex[1]] = vertex[2]
        self.delta_func = delta_func
    # check_string function checks if the given string could be accepted by the mentioned machine or not
    # and returns a string that demonstrates the result        
    def check_string(self, string) :
        legal = True
        current_state = self.initial_state
        for i in string :
            if i not in self.alphabet : legal = False
            current_state = self.delta_func[current_state][i]
        if current_state not in self.final_states : legal = False
        return  str(string) + ' can ' + ('not ' if not legal else '') + 'be accepted by this machine ;)'