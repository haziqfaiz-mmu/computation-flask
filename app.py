from flask import Flask, render_template, request, url_for, flash, redirect
import json
import sys

app = Flask(__name__)
app.config["SECRET_KEY"] = '48ea7d330380ad0bdc892ccbb2bcaaff3e59ca6b90a2da09'




@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        grammar = request.form['content']
        if not grammar:
            flash("Grammar is required")
        else:
            return redirect(url_for('cfgnfasolution'))
   
    return render_template('cfgnfa.html')

@app.route('/cfgnfasolution',methods=('GET','POST'))
def cfgnfasolution():
    grammar = request.form['content']
    return render_template('cfgnfa.html',grammar=grammar)

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