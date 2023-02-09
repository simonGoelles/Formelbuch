from flask import Flask, request, redirect, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model import Formel, Category
db = SQLAlchemy()

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/simon/Desktop/Pain/Stress/Ulmer3Formelheft/Formelbuch/Formel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

migrate = Migrate(app, db)

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
        mycategory = request.form['mycategory']
        _category = Category(catname=mycategory)
        db.session.add(_category)
        db.session.commit()
        formel = Formel(formeldescription=formeldescription, formelsigns=formelsigns, categoryid=_category.id)
        print(_category.id)
        db.session.add(formel)
        db.session.commit()
        return redirect('/data')


@app.route("/data/<string:category>")
def category_data(category):
    _category = db.session.query(Category).filter(Category.catname==category).all()[0]
    formel = db.session.query(Formel).filter(Formel.categoryid==_category.id).all()
    return render_template("data.html", formel=formel)


@app.route('/data')
def RetrieveDataList():
    formel = db.session.query(Formel).all()
    return render_template('data.html',formel = formel)


@app.route('/data/<int:id>', methods=["GET", "POST"])
def RetrieveSingleFormel(id):
    formel = db.session.query(Formel).filter(Formel.id==id).all()[0]
    if formel!=None:
        if request.method == "POST":
            action = request.form.get("action")
            if action == "update":
                return render_template('update.html', formel = formel)
            if action == "delete":
                return render_template('delete.html', formel = formel)
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
    formel = db.session.query(Formel).filter(Formel.id==id)
    if request.method == 'POST':
        if formel!=None:
            formel.update({'formeldescription': request.form['formeldescription'], 'formelsigns': request.form['formelsigns']})
            db.session.commit()
            return redirect("/data")
    return render_template('update.html', formel = formel)


app.run(debug=True)

