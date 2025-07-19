#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_dict={'Name':["a","b","c","d","e","f","g"],
        'age':[20,27,35,45,55,43,35],
        'designation':["VP","CEO","CFO","VP","VP","CEO","MD"]}

import pandas as pd
import numpy as np
df=pd.DataFrame(my_dict)
df


# In[2]:


df.to_csv('Csv example')
df


# In[3]:



con = sqlite3.connect("D:/Datasets/port")
df_csv=pd.read_csv('Csv example')
df_csv


# In[4]:


df.to_csv('CSV Ex',index=False)
df_csv=pd.read_csv('CSV Ex')
df_csv


# In[5]:





# In[6]:


import pandas as pd 
Location = "D:\Data\student-mat.csv"
df=pd.read_csv(Location, header=None)
df.head()


# In[7]:


import pandas as pd 
Location = "D:\Data\student-mat.csv"
df=pd.read_csv(Location)
df.head()


# In[9]:


import pandas as pd
Location = "D:\Data\student-mat.csv"
df = pd.read_csv(Location, names=['Rollno','Names','Grades'])
df.columns = ['Rollno','Names','Grades']
df.head()


# In[10]:


import pandas as pd
names = ['Bob','Jay','Marry','john','mel']
grades = [72,78,74,76,79]
bsdegrees = [1,0,1,1,1]
msdegrees = [2,3,1,0,1]
phdegrees = [0,1,0,2,1]
Degrees = zip(names,grades,bsdegrees,msdegrees,phdegrees)
columns = ['Names','Grades','BS','MS','phD']
df = pd.DataFrame(data= Degrees,columns=columns)
df


# In[19]:


import pandas as pd 
location="D:/Data/student-mat.xlsx"
df=pd.read_excel(location)

df.columns=['first','last','last','cell','age','hrs','addr','grd']
df.head()


# In[20]:


import pandas as pd 
location = "C:\Users\admin\Downloads\gradedata.xlsx"
df = pd.read_excel(location)

df.columns = ['first','last','last','cell','age','hrs','addr','grd']
df.head()


# In[22]:


import pandas as pd 
location = "C:/Users/admin/Downloads/gradedata.xlsx"
df = pd.read_excel(location)

df.columns = ['first','last','last','cell','age','hrs','addr','grd']
df.head()


# In[2]:


import sqlite3
con = sqlite3.connect("C:/Users/admin/Desktop/Datasets/portal_mammals.sqlite")
cur = con.cursor()

cur.execute('SELECT plot_id FROM plots WHERE plot_type="Control"')
print(cur.fetchall())

cur.execute('SELECT species FROM species WHERE taxa="Bird"')
print(cur.fetchone())

con.close()

            


# In[1]:


import sqlite3
import pandas as pd
con = sqlite3.connect("C:/Users/admin/Desktop/Datasets/portal_mammals.sqlite")
df = pd.read_sql_query("SELECT * FROM surveys", con)
print(df.head())

con.close()

            


# In[5]:


import sqlite3
conn = sqlite3.connect("TestDB1.db")
c = c=conn.cursor()


# In[6]:


c.execute("CREATE TABLE CARS2(Brand text, Price number)")
conn.commit()


# In[8]:


df.to_sql("CARS2",conn,if_exists='replace',index=False)
df


# In[10]:


c.execute('SELECT Brand,max(Price) from CARS2')
df= Dataframe(c.fetchall(),column=["Brand","Price"])
df


# In[2]:


import pandas as pd
import os
import sqlite3 as lite 
from sqlalchemy import create_engine


# In[3]:


studentId=["rj101","rj150","rj134","rj70"]
LName=["Chavan","Paul","Bisoi","Rai"]
SName=["Saurabh","Giftson","Vikas","Radha"]
Department=["Bms","Bcom","BscCS","BscIT"]
Email=["100rabh@gmail.com","gift01@gmail.com","vik21@gmail.com","rad01@gmail.com"]


# In[4]:


studata= zip(studentId,SName,LName,Department,Email)


# In[5]:


df=pd.DataFrame(data=studata,columns=["StudentId","SName","LName","Department","Email"])
df


# In[6]:


df.to_csv("students.csv", index=False)
df_read = pd.read_csv("students.csv")
df_read


# In[9]:


df.to_excel("stud.xlsx", index=False)


# In[10]:


db_filename=r"studentdata.db"
con=lite.connect(db_filename)
df.to_sql("student",con,schema=None,if_exists="replace",index=True,index_label=None,chunksize=None,dtype=None)
con.close()
db_file=r"studentdata.db"
engine=create_engine(r"sqlite:///{}" .format(db_file))
sql="SELECT * from student"
studf=pd.read_sql(sql,engine)
studf


# # Data preprocessing

# In[1]:


import numpy  as np
import pandas as pd


# In[2]:


state=pd.read_csv("C:/Users/admin/Desktop/Datasets/US_violent_crime.csv")
state


# In[4]:


def some_func(x):
    return x*2
state.apply(some_func)
# state.apply(lambda n: n*2)


# In[5]:


state.transform(func = lambda x: x*10)


# In[7]:


#using groupby
mean_purchase=state.groupby("State")["Murder"].mean().rename("User_Mean").reset_index()
print(mean_purchase)


# In[9]:


mean=state.merge(mean_purchase)
mean


# In[10]:


#checking for missing value
print(state.isnull().sum())


# In[16]:


import numpy  as np
import pandas as pd
cols=["col0","col1","col2","col3","col4"]
rows=["rows0","rows1","rows2","rows3","rows4"]
data=np.random.randint(0,100,size=(5,5))
df=pd.DataFrame(data,columns=cols,index=rows)
df.head()


# In[17]:


df.iloc[1,1]


# In[19]:


df.iloc[3,3]=0
df.iloc[1,2]=np.nan
df.iloc[1,2]=np.nan
df["cols5"]=0
df["cols6"]=np.nan
df.head()


# In[23]:


df.loc[:,df.all()]


# In[24]:


df.loc[:,df.any()]


# In[25]:


df.loc[:,df.isnull().any()]


# In[28]:


df.loc[:,df.notnull().all()]


# In[31]:


df.dropna(how="all",axis=0)


# In[34]:


df.fillna(df.sum())


# In[37]:


import pandas as pd
import numpy as np
import random
data = pd.DataFrame({
    "C":[random.choice(("a","b","c")) for i in range(1000000)],
    "A":[random.randint(1,10) for i in range(1000000)],
    "B":[random.randint(1,10)  for i in range(1000000)]
})
data


# In[39]:


v=  data.groupby("C")["A"].mean()
v


# In[40]:


mean = data.groupby("C")["A"].mean().rename("D").reset_index()
mean


# In[41]:


df_1 = data.merge(mean)
df_1


# In[ ]:




