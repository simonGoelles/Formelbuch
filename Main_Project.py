from flask import Flask, request, redirect, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model import Formel, Category
import sys

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/simon/Desktop/Pain/Stress/Ulmer3Formelheft/Formelbuch/Formel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

migrate = Migrate(app, db)


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('Createpage.html')

    if request.method == 'POST':
        formeldescription = request.form['formeldescription']
        formelsigns = request.form['formelsigns']
        mycategory = request.form['mycategory']
        _category = None
        try:
            _category = db.session.query(Category).filter(Category.catname==mycategory).all()[0]
        except:
            pass
        if not _category:
            _category = Category(catname=mycategory)
            db.session.add(_category)
            db.session.commit()
        formel = Formel(formeldescription=formeldescription, formelsigns=formelsigns)
        _category.formel.append(formel)
        db.session.add(formel)
        db.session.commit()
        return redirect('/data')


@app.route("/data/<string:category>")
def category_data(category):
    _category = db.session.query(Category).filter(Category.catname==category).all()
    if not _category:
        return "The requested category does not exist"
    formel = db.session.query(Formel).filter(Formel.categoryid==_category[0].id).all()
    return render_template("data.html", formel=formel, category=_category)



@app.route('/data')
def RetrieveDataList():
    formel = db.session.query(Formel).all()
    _category = db.session.query(Category).all()
    return render_template('data.html', formel=formel, category=_category)


@app.route('/data/<int:id>', methods=["GET", "POST"])
def RetrieveSingleFormel(id):
    formel = db.session.query(Formel).filter(Formel.id==id).all()[0]
    if not formel:
        return f"Formel with id ={id} not found"
    if request.method == "POST":
        action = request.form.get("action")
        if action == "update":
            return render_template('update.html', formel=formel, id=id)
        if action == "delete":
            return render_template('delete.html', formel=formel, id=id)
    return render_template('singleData.html', formel=formel)


@app.route('/data/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    formel = db.session.query(Formel).filter(Formel.id==id).first()
    if formel:
        if request.method == 'POST':
            db.session.delete(formel)
            db.session.commit()
            return redirect('/data')
        return render_template('delete.html', formel=formel, id=id)
    else:
        abort(404)


@app.route('/data/<int:id>/update', methods=['GET', 'POST'])
def Update(id):
    formel = db.session.query(Formel).filter(Formel.id==id).first()
    if request.method == 'POST':
        if formel:
            formel.formeldescription = request.form['formeldescription']
            formel.formelsigns = request.form['formelsigns']
            db.session.commit()
            return redirect("/data")
    return render_template('update.html', formel = formel, id=id)



app.run(debug=True)
