from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Supõe-se que a variável ENV seja definida externamente (p.ex., via linha de comando ou configuração do servidor)
env = os.getenv('ENV')  # Padrão para 'dev' se não definido

if env == 'prod':
    load_dotenv(dotenv_path='.env.prod')
else:
    load_dotenv(dotenv_path='.env.dev')

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    salary = Column(Float)
    age = Column(Integer)
    department = Column(String)

def create_table():
    Base.metadata.create_all(engine)