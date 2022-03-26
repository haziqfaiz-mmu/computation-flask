from automathon import NFA

def drawNFA(Q, sigma, delta, initialState, F):
    automata = NFA(Q, sigma, delta, initialState, F)
    ## This is an example about creating a NFA with the library
    automata.view("NFA Visualization")