from pandas.io import sql
import pandas as pd
import sqlalchemy as db
from datetime import datetime, date
import numpy as np
from scipy import stats
import pymysql

df = pd.read_csv("co2.csv")
print(df.head(10))
df.shape
print(df.shape)

df.info()
print(df.info())

base_user="root"
base_pass="0000" 
base_ip="localhost"
base_name="ambiente" #informamos o nome do database no MySQL
base_connection = db.create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.format(base_user,base_pass,base_ip,base_name))

connection = base_connection.connect()
metadata = db.MetaData()

df.to_sql('co2', connection)