from flask import Flask, render_template, request, url_for, flash, redirect
import json
import sys

app = Flask(__name__)
app.config["SECRET_KEY"] = '48ea7d330380ad0bdc892ccbb2bcaaff3e59ca6b90a2da09'

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]



@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        grammar = request.form['content']
        if not grammar:
            flash("Grammar is required")
        else:
            return redirect(url_for('index'))

            
    return render_template('cfgnfa.html')

@app.route('/nfacfg', methods=('GET', 'POST'))
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



if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)