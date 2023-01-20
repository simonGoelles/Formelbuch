from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model import Formel, Kategorie, Kapitel

engine = create_engine("sqlite:///Formel.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

for _ in range(5):
    session.add(Formel(Formel="a + b", Description="this a decription, test", Ergebnis="this a Ergebnis, test", Kategorie_id=1))
    session.add(Kategorie(Kategorie="This is a Kategorie, test", Kapitel_id=1))
    session.add(Kapitel(Kapitel="this a Kapitel"))

session.commit()
