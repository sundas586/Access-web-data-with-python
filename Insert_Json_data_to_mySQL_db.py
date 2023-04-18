#!/usr/bin/env python
# coding: utf-8

# Insert Json data to mysql using SqlAlchemy & Pandas

# * sqlalchemy.create_engine() --> for database connection
# * engine.execute() --> to run mysql querues ondatabase
# * pd.read_json() --> to read json file and store as pandas dataframe
# * df.to_sql() --> to save dataframe in mysql
# * .fetchall() #fetchone() --> to fetch records from mysqlDB
# 

# In[22]:


import pandas as pd
import sqlalchemy
import pymysql


# In[23]:


pip install pymysql


# In[24]:


import pymysql


# In[8]:


# Create a database engine
engine = sqlalchemy.create_engine('mysql+pymysql://root:smart18!!!@localhost/')


# In[9]:


# Create a database
engine.execute("CREATE DATABASE myJsonToMySqlDB")


# In[15]:


# Create a database
engine.execute("create table if not exists myJsonToMySqlDB.employees( name varchar(255), age int, salary int);")


# In[12]:


# Connect to the new database we created
engine = sqlalchemy.create_engine('mysql+pymysql://root:smart18!!!@localhost/myJsonToMySqlDB')


# In[18]:


# read the JSON file into a pandas DataFrame
df = pd.read_json(r'C:\Users\sundas.asif\Desktop\employees.json')


# In[19]:


# write the DataFrame to a MySQL table
df.to_sql(name='employees', con=engine, if_exists='replace', index=False)


# In[21]:


# confirm that the data was loaded successfully
result = engine.execute('SELECT * FROM employees').fetchall() #fetchone()
print(result)


# In[ ]:




