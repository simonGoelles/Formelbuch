from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BIGINT, VARCHAR, INTEGER
from sqlalchemy.schema import CreateTable

engine = create_engine('sqlite:///Formel.db', echo=True)
meta = MetaData()
Base = declarative_base()


class Formel(Base):
    __tablename__ = 'Formel'
    id = Column(Integer, primary_key=True)
    Kategorie_id = Column(Integer, ForeignKey("Kategorie.id"))
    Formel = Column(String)
    Description = Column(String)
    Ergebnis = Column(String)


class Kategorie(Base):
    __tablename__ = 'Kategorie'
    id = Column(Integer, primary_key=True)
    Kapitel_id = Column(Integer, ForeignKey("Kapitel.id"))
    Kategorie = Column(String)


class Kapitel(Base):
    __tablename__ = 'Kapitel'
    id = Column(Integer, primary_key=True)
    Kapitel = Column(String)


Base.metadata.create_all(engine)
