from flask import Flask, render_template, request, url_for, flash, redirect
import json, os,ast
import sys
import validateNFA, drawNFA, NFAtoCFG, CFGtoNFA
from nltk.parse import RecursiveDescentParser

app = Flask(__name__)
app.config["SECRET_KEY"] = '48ea7d330380ad0bdc892ccbb2bcaaff3e59ca6b90a2da09'

maingrammar=""


@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('cfgnfa.html')

@app.route('/cfgnfasolution',methods=('GET','POST'))
def cfgnfasolution():
    global maingrammar
    string = request.form['grammar'].replace("\r","").replace("\t","").replace(" ","")
    maingrammar = request.form['grammar']
    Q = CFGtoNFA.getState(string)
    sigma = CFGtoNFA.getSigma(string,Q)
    initialState = CFGtoNFA.getInitialState(string,Q)
    delta = CFGtoNFA.getDelta(string,Q,sigma)
    Q,finalState,delta = CFGtoNFA.getFinalState(string,sigma,Q,delta)


    drawNFA.drawNFA(Q, sigma, delta, initialState, finalState)
    os.replace("/home/haziq/Documents/computation-flask/NFA Visualization.gv.png", "/home/haziq/Documents/computation-flask/static/NFA Visualization.gv.png")
    return render_template('cfgnfa.html',Q=Q,sigma=sigma, initialState=initialState, finalState=finalState,delta=delta)

@app.route('/validate/',methods=('GET','POST'))
def validate():
    global maingrammar
    grammar = maingrammar.replace("$","")
    string = request.form['validate']

    result = [];
    string = string.replace("\r","")
    string = string.split("\n")

    rd = RecursiveDescentParser(grammar)
    for i in string:
        result.append(validateNFA.readGrammar(rd,i))
    #result.append(validateNFA.readGrammar(maingrammar,string))
    
    return render_template('cfgnfa.html',string=string,grammar= maingrammar, result=result)

@app.route('/nfacfg/', methods=('GET', 'POST'))
def index2():
    return render_template('nfacfg.html')

@app.route('/nfacfgsolution/', methods=('GET', 'POST'))
def nfacfgsolution():
    global maingrammar
    
    alphabet = set(request.form['alphabet'].replace(" ","").split(","))
    states = set( request.form['Q'].split(","))
    delta = (request.form['delta']).replace("'",'"').replace("/r","").replace("/n","")
    delta = (json.loads((delta)))
    initialState = request.form['initialState'].split(",")
    finalState = request.form['finalState'].split(",")

    regularGrammar = NFAtoCFG.NFAtoCFG(states,alphabet,delta)
    maingrammar = regularGrammar

    drawNFA.drawNFA(Q, alphabet, delta, initialState, finalState)
    os.replace("/home/haziq/Documents/computation-flask/NFA Visualization.gv.png", "/home/haziq/Documents/computation-flask/static/NFA Visualization.gv.png")

    return render_template('nfacfg.html',alphabet =alphabet, Q=states, delta=delta, regularGrammar=regularGrammar)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)