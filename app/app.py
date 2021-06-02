from typing import List, Dict
from flask import Flask
import json
from sqlalchemy import create_engine, MetaData, Table, Column, Float, Integer, String, ForeignKey
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.dialects.mysql import DATETIME
import logging
# from .models import db


config = {
    'host': 'db',
    'port': '3306',
    'user': 'root',
    'password': 'root',
    'database': 'classicmodels'
}

db_user = config.get('root')
db_pwd = config.get('root')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')


connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'

engine = create_engine(connection_str)
connection = engine.connect()
print('------MYSQL Docker Container Python connection ok -----')