#!/usr/bin/env python
# coding: utf-8

# In[1]:


file = open('data.csv', 'r')
data = file.readlines()
file.close()
income = []
outcome = []


# In[2]:


for line in data:
    line = line.split(',')
    if line[1] == '933156729':
        outcome.append(line)
    if line[2] == '933156729':
        income.append(line)


# In[3]:


X = 0
k_out_before = 3
k_out_after = 2
k_inc_before = 0
k_inc_after = 2
k_sms = 2


# In[4]:


for call in outcome:
    time = call[0][-8:]
    if int(call[4]) > 50:
        X += (int(call[4]) - 50) * k_sms
    if time >= '00:30:00':
        X += float(call[3]) * k_out_after
    elif time < '00:30:00':
        minutes = 30 - int(time[3:5])
        X += minutes * k_out_before + (float(call[3]) - minutes) * k_out_after


# In[5]:


for call in income:
    time = call[0][-8:]
    dur = float(call[3])
    if time >= '00:30:00':
        X += dur * k_in_after
    elif time < '00:30:00':
        minutes = 30 - int(time[3:5])
        if minutes > dur:
            X += dur * k_inc_before
            continue
        X += minutes * k_inc_before + (float(call[3]) - minutes) * k_inc_after


# In[6]:


print('Итоговая сумма: ', X)


# In[7]:


def countPhone():
    return X

