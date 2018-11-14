# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[2]:


url ='https://www.worldatlas.com/as/in/cities-in-india.html'

## Fetch the webpage
r = requests.get(url)
print type(r)


# In[3]:


r.status_code


# In[5]:


info = r.text


# In[6]:


soup = BeautifulSoup(r.text, 'html.parser')


# In[7]:


city=[]


# In[8]:


table_inf = soup.find_all('tbody')


# In[9]:


doc=table_inf[0]


# In[10]:


gop=doc.find_all('tr')


# In[11]:


City=[]


# In[12]:


for ix in range(len(gop)):
    k=gop[ix].find_all('td')
    s=k[0].encode('utf-8')
    f=s.split(".html")
    l=f[1]
    k=0
    for ixx in range(len(l)):
        if l[ixx]=='<' and l[ixx+2]=='a':
            City.append(l[2:ixx])
        
        
    

    
    


# In[13]:


import pandas as pd


# In[14]:


data=pd.DataFrame(City,columns=["CITY"])


# In[15]:


data.to_csv("city.csv",header=None,index=False)


# In[16]:


pd.read_csv("city.csv")


# In[134]:


len(city)
