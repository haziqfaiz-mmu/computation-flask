from flask import Flask, render_template, request, url_for, flash, redirect
import json
import sys
import validateNFA, drawNFA, NFAtoCFG, CFGtoNFA

app = Flask(__name__)
app.config["SECRET_KEY"] = '48ea7d330380ad0bdc892ccbb2bcaaff3e59ca6b90a2da09'




@app.route('/', methods=('GET', 'POST'))
def index():
    
   
    return render_template('cfgnfa.html')

@app.route('/cfgnfasolution',methods=('GET','POST'))
def cfgnfasolution():
    string = request.form['grammar']
    Q = CFGtoNFA.getState(string)
    sigma = CFGtoNFA.getSigma(string,Q)
    initialState = CFGtoNFA.getInitialState(string,Q)
    finalState = CFGtoNFA.getFinalState(string,sigma)
    delta = CFGtoNFA.getDelta(string,Q,sigma)
    return render_template('cfgnfa.html',Q=Q,sigma=sigma, initialState=initialState, finalState=finalState,delta=delta)


@app.route('/nfacfg/', methods=('GET', 'POST'))
def index2():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index2'))
    return render_template('nfacfg.html')

@app.route('/nfacfgsolution/',methods=('GET','POST'))
def nfacfgsolution():
    return



if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)