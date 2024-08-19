from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date,Time

Base = declarative_base()

class Todo(Base):
    __tablename__= "TASKS"
    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String(100))  
    desc =Column(String(500))  
    complete = Column(Boolean) 
    date = Column(Date) 
    time = Column(Time)
    priority = Column(String(255))
    category = Column(String(255))

    def __init__(self, task, desc, complete, date, time, priority, category):
       self.task= task
       self.desc = desc
       self.complete = complete
       self.date = date
       self.time = time
       self.priority = priority
       self.category = category

