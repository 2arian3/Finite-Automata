# Finite-Automata
The main assignment of the theory of machines and languages course.<br>
It's a simple command-line simulation of the finite automata using python's built-in data structures.<br>
In **dfa.py** script we have DFA class with a constructor and a simple membership method which checks whther the input string can be accepted by the dfa machine or not.<br>
In **nfa.py** script we have a method that returns the equivalent dfa machine of the nfa machine based on a simple algorithm.<br>
## DFA and NFA class constructor parameters
* alphabet : The list of legal inputs.
* states : A list containing all the possible states.
* initial_state : Starting state(must be in the states).
* final_states : The ending states(must be in the states).
* moves : A list containing all of the possible moves based on the input and current state.
## Example
We have the following nfa:
```
alphabet : ['a', 'b', 'c']
states : ['q0', 'q1', 'q2']
initial_state : 'q0'
final_states : 'q2'
moves : [['q0', 'a', 'q0'], 
         ['q0', 'λ', 'q1'], 
         ['q1', 'b', 'q1'], 
         ['q1', 'λ', 'q2'], 
         ['q2', 'c', 'q2']]
```
The equivalent dfa machine of this nfa calculated in convert_to_dfa is:
```
alphabet : ['a', 'b', 'c']
states : ['q0', 'q1', 'q2', 'q3', 'q4']
initial_state : 'q0'
final_states : ['q0', 'q1', 'q2', 'q3']
moves : [['q0', 'a', 'q1'], 
         ['q0', 'b', 'q2'], 
         ['q0', 'c', 'q3'], 
         ['q1', 'a', 'q1'], 
         ['q1', 'b', 'q2'], 
         ['q1', 'c', 'q3'], 
         ['q2', 'a', 'q4'], 
         ['q2', 'b', 'q2'], 
         ['q2', 'c', 'q3'], 
         ['q3', 'a', 'q4'], 
         ['q3', 'b', 'q4'], 
         ['q3', 'c', 'q3'], 
         ['q4', 'a', 'q4'], 
         ['q4', 'b', 'q4'], 
         ['q4', 'c', 'q4']]
```


