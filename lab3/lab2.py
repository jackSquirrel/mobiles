#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import datetime
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


file = open('traffic.csv', 'r')
data = file.readlines()
file.close()
trafic = 0
time = [] 
bit = []
time_data = []


# In[3]:


for line in data:
    line = line.split(',')
    if line[0] == 'Summary\n':
        break
    if line[4] == '192.168.250.3' or line[3] == '192.168.250.3':
        trafic += int(line[12])
        time_data.append((datetime.datetime(int(line[0][0:4]), int(line[0][5:7]), int(line[0][8:10]), int(line[0][-8:-6]), int(line[0][-5:-3]), int(line[0][-2:])), int(line[12])))


# In[4]:


sorted_time_data = sorted(time_data, key=lambda traf: traf[0])


# In[5]:


for traf in sorted_time_data:
    time.append(traf[0])
    bit.append(traf[1])


# In[6]:


plt.figure(figsize=(20,10))
plt.plot(time, bit)


# In[7]:


Summ = (trafic / 1024 / 1024) * 3
print('Трафик на сумму:', round(Summ, 2), 'руб')


# In[ ]:


def countInternet():
    return round(Summ, 2)

