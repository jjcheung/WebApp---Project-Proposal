from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('proj-list.html')

@app.route('/form')
def proj_form():
    return render_template('proj-form.html')

@app.route('/submit', methods = ['POST'])
def generate():
    submission = request.form['submit']
    if submission == 'Submit Proposal':
        data = report()
        return render_template('proj-list.html', data=data)
    else:
        insert(request.form)
        return 'Project Proposal submitted.'

@app.route("/report", methods=['GET'])
def report():
    conn = sqlite3.connect("app.db")
    cursor = conn.execute('SELECT ID, title, description, proposer FROM Project;')
    data = []
    for record in cursor:
        data.append(record)
    conn.close()
    return render_template('proj-list.html', data=data)


app.run(host='0.0.0.0', port=81)