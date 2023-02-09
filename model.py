from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BIGINT, VARCHAR, INTEGER, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from base import Base

engine = create_engine('sqlite:///Formel.db', echo=True)
meta = MetaData()
Base = declarative_base()
db = SQLAlchemy()

class Category(Base):
    __tablename__ = 'Category'

    id = db.Column(db.Integer, primary_key=True)
    catname = db.Column(db.String(100), nullable=False)
    formel = relationship("Formel")

    def __init__(self, catname):
        self.catname = catname

    def __repr__(self) -> str:
        return f"{self.catname}"

class Formel(Base):
    __tablename__ = 'Formel'
    
    id = db.Column(db.Integer, primary_key=True)
    formelsigns = db.Column(db.String(100), nullable=False)
    formeldescription = db.Column(db.String(300), nullable=False)
    categoryid = db.Column(db.Integer, ForeignKey("Category.id"), nullable=False)

    def __init__(self, formeldescription, formelsigns, categoryid):
        self.formeldescription = formeldescription
        self.formelsigns = formelsigns
        self.categoryid = categoryid

    def __repr__(self) -> str:
        return f"{self.formeldescription}:{self.formelsigns}:{self.categoryid}"

Base.metadata.create_all(engine)