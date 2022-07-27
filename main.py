from flask import Flask, request, render_template, url_for, redirect
import sqlite3
import model

app = Flask(__name__)


@app.route('/')
def index():
    data = model.Project.select_all()
    return render_template('proj-list.html', data=data)


@app.route('/form')
def proj_form():
    return render_template('proj-form.html')


@app.route('/submit', methods = ['POST'])
def generate():
    data = request.form
    model.Project(data['project_name'], data['project_description'], data['proposer_name'])
    return redirect(url_for('index'))
    #return 'Data inserted'


@app.route("/report", methods=['GET'])
def report():
    data = model.Project.select_all()
    return render_template('proj-list.html', data=data)


@app.route("/delete/<pid>", methods=['GET'])
def delete(pid):
  model.Project.delete(int(pid))
  return redirect(url_for("index"))


app.run(host='0.0.0.0', port=81)
