import pandas as pd
import mysql.connector
import sqlalchemy
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String



engine = create_engine(
    'mysql+mysqlconnector://coolspammail:coolspammail-pass@db4free.net/coolspammail')

Base = declarative_base()


class User(Base):
    __tablename__ = 'alchemy'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)


print(User.__table__)
Table('alchemy', MetaData(bind=None),
    Column('id', Integer(), table="alchemy", primary_key=True, nullable=False),
    Column('name', String(), table="alchemy"),
    Column('fullname', String(), table="alchemy"),
    Column('nickname', String(), table="alchemy"), schema=None)
