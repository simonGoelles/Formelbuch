from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from model import Formel
db = SQLAlchemy()
 
app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/simon/Desktop/Pain/Stress/Ulmer3 (Formelheft)/Formelbuch/Formel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('Createpage.html')
 
    if request.method == 'POST':
        formeldescription = request.form['formeldescription']
        formelsigns = request.form['formelsigns']
        formel = Formel(formeldescription=formeldescription, formelsigns=formelsigns)
        db.session.add(formel)
        db.session.commit()
        return redirect('/data')

@app.route('/data')
def RetrieveDataList():
    formel = Formel.query.all()
    return render_template('datalist.html',formel = formel)


@app.route('/data/{id}}')
def RetrieveSingleEmployee(id):
    formel = Formel.query.filter_by(id=id).first()
    if formel:
        return render_template('data.html', formel = formel)
    return f"formel with id ={id} doesn't exist"


app.run(debug=True)