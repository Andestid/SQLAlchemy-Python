from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'

    cedula = Column("cedula", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, cedula, firstname, lastname, gender, age):
        self.cedula = cedula
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age
    
    def __repr__(self):
     return f"({self.cedula}) {self.firstname} {self.lastname} ({self.gender}, {self.age})"
    
engine = create_engine("sqlite:///my.db.db",echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(5666,"Mike","john","Male","13")
session.add(person)
session.commit()

p1 = Person(44,"sads","john","Male",13)
p2 = Person(34,"gfgfg","john","Male",13)
p3 = Person(24,"e","john","Male",1)

session.add(p1)
session.add(p2)
session.add(p3)
session.commit()

results = session.query(Person).all()
print (results)