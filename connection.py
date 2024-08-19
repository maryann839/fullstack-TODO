from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus


username = 'root'
password = '@Nadiaann839'
dbname = 'todo'

encoded_password = quote_plus(password)



path = f"mysql://{username}:{encoded_password}@localhost:3306/{dbname}"

database = create_engine(path)

Session =sessionmaker(bind=database)
session = Session()