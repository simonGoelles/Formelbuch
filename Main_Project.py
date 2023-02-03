from flask import Flask, request, redirect, render_template, abort
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
    formel = db.session.query(Formel).all()
    return render_template('data.html',formel = formel)


@app.route('/data/<int:id>')
def RetrieveSingleFormel(id):
    formel = db.session.query(Formel).filter(Formel.id==id).all()[0]
    if formel!=None:
        return render_template('singleData.html', formel = formel)
    return f"formel with id ={id} doesn't exist"

@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    formel = db.session.query(Formel).filter(Formel.id==id).all()[0]
    if request.method == 'POST':
        if formel!=None:
            db.session.delete(formel)
            db.session.commit()
            return redirect('/data')
        abort(404)
    return render_template('delete.html')

@app.route('/data/<int:id>/update', methods=['GET', 'POST'])
def Update(id):
    formel = db.session.query(Formel).filter(Formel.id==id).all()[0]
    if request.method == 'POST':
        if formel!=None:
            db.session.update(formel)
            db.session.commit()
            return redirect("/data")
    return render_template('update.html', formel = formel)


app.run(debug=True)