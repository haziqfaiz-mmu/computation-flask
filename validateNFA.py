from nltk.parse import RecursiveDescentParser
from nltk import CFG

grammar = CFG.fromstring("""
S -> 'a' S | T
T -> 'b' T | 
""")


rd = RecursiveDescentParser(grammar)

sentence =  ['aaaabbba','aaa']
result=[]

def readGrammar(rd,sentence):
    rd = RecursiveDescentParser(grammar)
    for word in sentence:
        correct_grammar=False
        for t in rd.parse(sentence):
            correct_grammar=True
    return correct_grammar

for i in sentence: 
    result.append(readGrammar(rd,i))

print(result)