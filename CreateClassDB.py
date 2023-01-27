from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BIGINT, VARCHAR, INTEGER
from sqlalchemy.schema import CreateTable
from flask_sqlalchemy import SQLAlchemy
Base = declarative_base()

class Formel(Base):
    __tablename__ = 'Formel'
    id = Column(Integer, primary_key=True)
    Kategorie_id = Column(Integer, ForeignKey("Kategorie.id"))
    Formel = Column(String)
    Description = Column(String)
    Ergebnis = Column(String)

    def __init__(self, formeldescription, formelsigns):
        self.formeldescription = formeldescription
        self.formelsigns = formelsigns
