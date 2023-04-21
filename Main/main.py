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
    

class Thing(Base):
   __tablename__ = 'Things'

   tid = Column("tid",Integer, primary_key=True)
   description = Column("description", String)
   owner = Column("owner", Integer, ForeignKey("people.cedula"))

   def __init__(self, tid, description, owner):
      self.tid = tid
      self.description = description
      self.owner = owner
   def __repr__ (self):
        return f"({self.tid}) {self.description} owned by {self.owner}"

engine = create_engine("sqlite:///my.db.db",echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# person = Person(5666,"Mike","john","Male","13")
# session.add(person)
# session.commit()

# p1 = Person(44,"sads","john","Male",13)
# p2 = Person(34,"gfgfg","john","Male",13)
# p3 = Person(24,"e","john","Male",1)

# session.add(p1)
# session.add(p2)
# session.add(p3)
# session.commit()

results = session.query(Person).all()
print (results)

results = session.query(Person).filter(Person.age < 12)
for r in results:
   print (r)

#t1 = Thing(123,"holaaaa",5666)
#session.add(t1)
#session.commit()

results = session.query(Thing).all()
print (results)