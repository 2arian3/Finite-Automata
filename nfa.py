# Arian Boukani 9731012
# nondeterministic finite automata class
import dfa
class NFA :
    # alphabet is the list of the legal inputs
    # states is a list that contains the name of the possible states
    # final_states is a list because we might have a machine with more than one final state
    # moves is the list of moves that each component is a list with three components
    # the first one is the name of the starting state, the second component is the given input and the last one is the result state
    def __init__(self, alphabet, states, initial_state, final_states, moves) :
        self.alphabet = alphabet
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.moves = moves
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
        for move in moves :
            if move[1] not in delta_func[move[0]] :
                if move[1] not in self.alphabet : move[1] = 'lambda'
                delta_func[move[0]][move[1]] = [move[2]]
            else : delta_func[move[0]][move[1]].append(move[2])   
        self.delta_func = delta_func
    # finding the lambda closure of the given state in the machine
    # result is a set of the states      
    def lambda_closure(self, state) :
        res = {state}
        for move in self.moves :
            if move[0] in res and move[1] not in self.alphabet :
                res.add(move[2])
        return res  
    # convert_to_dfa function returns and produces the equivalent dfa machine of the given nfa machine using lambda_closure function
    # with the same alphabet and same initial state but with different final_states and transition function
    def convert_to_dfa(self) :
        dfa_state_size = 1
        final_states = []
        dfa_final_states = []
        dfa_initial_state = 'q0'
        delta_prime_func = dict()
        # dfa_states just stores the name of the states. for example : ['q0', 'q1', ...]
        dfa_states = [dfa_initial_state]
        # since in the new dfa machine the states might be made up of several states of the nfa machine, and it might be a little bit
        # hard to store the new states as a list, i used dictionary to store the states in this format
        # for example : {'q0' : ['Q1', 'Q2'], 'q1' : ['Q0'], ...}
        # in this example q's are dfa's states and the Q's are nfa's state, but the list of the nfa states is the equivalent 
        dfa_states_name = dict()
        dfa_delta_func = dict()
        dfa_moves = []
        dfa_states_name[dfa_initial_state] = [self.initial_state]
        dfa_delta_func[dfa_initial_state] = dict()
        # first of all i find the new machine's final states which depend's on the nfa's final states
        for state in self.states :
            lamda_closure = self.lambda_closure(state)
            for s in lamda_closure :
                if s in self.final_states :
                    final_states.append(state)  
        # and then we use lambda_closure function to produce the delta prime transition function of the nfa state
        # which helps us to produce the result dfa machine                     
        for state in self.states :
            lambda_closure = self.lambda_closure(state)
            delta_prime_func[state] = dict()
            for alpha in self.alphabet :
                res = set()
                for s in lambda_closure :
                    # since in nfa machine we might have no transition for a state for the given input
                    # i used try in order not to result in exception
                    try :
                        tmp = self.delta_func[s][alpha]
                        for i in tmp :
                            res = res.union(self.lambda_closure(i))
                    except :
                        pass    
                delta_prime_func[state][alpha] = res
        # computing the new machine's delta transition function until there is no new state        
        for dfa_state in dfa_states :
            for alpha in self.alphabet :
                res = set()
                for state in dfa_states_name[dfa_state] :
                    res = res.union(delta_prime_func[state][alpha])
                found = False
                res = list(res)
                next_state = ''
                for name, state in dfa_states_name.items() :
                    if sorted(state) == sorted(res) :
                        found = True 
                        next_state = name 
                # if the result state is not in the dfa_states we will consider it as a new state                       
                if not found :
                    new_state_name = 'q' + str(dfa_state_size)
                    dfa_states.append(new_state_name)
                    dfa_states_name[new_state_name] = res
                    dfa_delta_func[new_state_name] = dict()
                    next_state = new_state_name
                    dfa_state_size += 1   
                dfa_delta_func[dfa_state][alpha] = next_state
        # computing the final states based on the new names
        for name, state in dfa_states_name.items() :
            for s in state :
                if s in final_states and name not in dfa_final_states:
                    dfa_final_states.append(name) 
        # producing the vertices in order to call the DFA class
        for current_state in dfa_states_name :
            for alphabet in self.alphabet :
                dfa_moves.append([current_state, alphabet, dfa_delta_func[current_state][alphabet]])
        return dfa.DFA(self.alphabet, dfa_states, dfa_initial_state, dfa_final_states, dfa_moves)    