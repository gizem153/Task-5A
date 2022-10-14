
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
start_time=time.time()
Base = declarative_base()
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres', echo = True)
Session = sessionmaker(bind = engine)
session = Session()

class GIRIS(Base):
    __tablename__ = 'GIRIS'
    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    password = Column(String(100), nullable=False)

class BUL(Base):
    __tablename__="BUL"
    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    password = Column(String(100), nullable=False)

def Generator(i):
  liste1 = []
  for i in range(i):
    fake=Faker()
    liste2=[]
    liste2.append(fake.email())
    liste2.append(fake.password())
    liste1.append(liste2)
  return liste1
Base.metadata.create_all(engine)
Generator(1000)

session.commit()

end_time=time.time()
print(end_time-start_time)


