from model import Formel
import pytest
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from model import Formel, Category
import Main_Project



@pytest.fixture
def client():

    db = SQLAlchemy()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/simon/Desktop/Pain/Stress/Ulmer3Formelheft/Formelbuch/Formel.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    ctx = app.app_context()
    ctx.push()
    yield app.test_client()
    ctx.pop()

def test_create(client):
    response = client.get('/')
    assert response.status_code == 200
    response = client.post('/', data={'formeldescription': 'test_formel_description', 'formelsigns': 'test_formel_signs', 'mycategory': 'test_category'})
    assert response.status_code == 302

def test_category_data(client):
    response = client.get('/data/test_category')
    assert response.status_code == 200
    response = client.get('/data/nonexistent_category')
    assert b"The requested category does not exist" in response.data

def test_RetrieveDataList(client):
    response = client.get('/data')
    assert response.status_code == 200

def test_RetrieveSingleFormel(client):
    formel = Formel(formeldescription='test_formel_description', formelsigns='test_formel_signs')
    formel.save()
    response = client.get(f'/data/{formel.id}')
    assert response.status_code == 200
    response = client.post(f'/data/{formel.id}', data={'action': 'update'})
    assert response.status_code == 200
    response = client.post(f'/data/{formel.id}', data={'action': 'delete'})
    assert response.status_code == 200
    response = client.get(f'/data/{formel.id + 1000}')
    assert b"Formel with id =" in response.data

def test_delete(client):
    formel = Formel(formeldescription='test_formel_description', formelsigns='test_formel_signs')
    formel.save()
    response = client.get(f'/data/{formel.id}/delete')
    assert response.status_code == 200
    response = client.post(f'/data/{formel.id}/delete')
    assert response.status_code == 302
    response = client.get(f'/data/{formel.id + 1000}/delete')
    assert response.status_code == 404

def test_Update(client):
    formel = Formel(formeldescription="formel 1", formelsigns="formelsigns 1")
    db.session.add(formel)
    db.session.commit()
    formel_id = formel.id
    response = client.post(f'/data/{formel_id}/update', data={'formeldescription': 'formel 2', 'formelsigns': 'formelsigns 2'}, follow_redirects=True)
    formel = db.session.query(Formel).filter(Formel.id == formel_id).first()
    assert formel.formeldescription == "formel 2"
    assert formel.formelsigns == "formelsigns 2"
    assert response.status_code == 200

def test_delete(client):
    formel = Formel(formeldescription="formel 1", formelsigns="formelsigns 1")
    db.session.add(formel)
    db.session.commit()
    formel_id = formel.id
    response = client.post(f'/data/{formel_id}/delete', follow_redirects=True)
    formel = db.session.query(Formel).filter(Formel.id == formel_id).first()
    assert formel == None
    assert response.status_code == 200