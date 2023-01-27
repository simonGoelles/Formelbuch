from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BIGINT, VARCHAR, INTEGER
from sqlalchemy.schema import CreateTable
from flask_sqlalchemy import SQLAlchemy
from CreateClassDB import Formel

engine = create_engine('sqlite:///Formelheft.db', echo=True)
meta = MetaData()
Base = declarative_base()
db = SQLAlchemy()

class Formel(db.Model):
    __tablename__= "Formel"

    id = db.Column(db.Integer, primary_key=True)
    formeldescription = db.Column(db.String())
    formelsigns = db.Column(db.String())

    def __init__(self, formeldescription, formelsigns):
        self.formeldescription = formeldescription
        self.formelsigns = formelsigns

    def __repr__(self) -> str:
        return f"{self.formeldescription}:{self.formelsigns}"

