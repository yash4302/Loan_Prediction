#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle


# In[2]:


df = pd.read_csv('credit_train.csv')
df = df[:100000]
df = df.drop_duplicates()
df = df.reset_index()
df = df.drop('index',axis=1)
df


# In[3]:


temp = df['Purpose'].str.capitalize()
df = df.drop(['Purpose'],axis = 1)
df2 = pd.concat([df,temp],axis = 1)
df2 = df2.drop(['Loan ID','Customer ID'],axis = 1)
df2


# In[4]:


x = df2['Home Ownership']
x = pd.DataFrame(x)
for i in range(0,len(x)):
    if x['Home Ownership'][i] == 'HaveMortgage':
         x.loc[i]['Home Ownership'] = 'Home Mortgage'

df2 = df2.drop(['Home Ownership'],axis=1)
df2 = pd.concat([df2,x],axis=1)
df2


# In[5]:


x = df2['Number of Credit Problems'].isnull()
for i in x:
    if i:
        print("Has Nulls")


# In[6]:


z = list(df['Years in current job'])


i = 0
# to remove signs
while i in range(0,89785):
    if z[i] is np.nan:
        pass
    else:
        for j in z[i]:
            if j == '+':
                z[i] = z[i].replace('+','')
            if j == '<': 
                z[i] = z[i].replace('<','')
            if j == ">":
                z[i] = z[i].replace('>','')
    i+=1
    

# to get only numbers
xz = []
for i in z:
    if i is np.nan:
        xz.append(np.nan)
    else:
        x = [int(s) for s in i.split() if s.isdigit()]
        xz.append(x[0])
xz

yearsx = np.array(xz)
years = pd.DataFrame(yearsx)
years.columns = ['Years']
years

df3 = pd.concat([df2,years],axis=1)
df3 = df3.drop(['Years in current job'],axis=1)
df3


# In[7]:


# fill nulls
credit_median = df3['Credit Score'].median()
income_median = df3['Annual Income'].median()
month_median = df3['Months since last delinquent'].median()
max_credit_median = df3['Maximum Open Credit'].median()
bankruptcies = 0
tax = 0
years_median = df3['Years'].median()

fill_nulls = {
    'Credit Score':credit_median,
    'Annual Income':income_median,
    'Months since last delinquent':month_median,
    'Maximum Open Credit':max_credit_median,
    'Bankruptcies':bankruptcies,
    'Tax Liens':tax,
    'Years':years_median
}

df3.fillna(value = fill_nulls,inplace=True)
df3


# In[8]:


df4 = pd.get_dummies(df3['Loan Status'], drop_first=True) # for loan status
df5 = pd.get_dummies(df3['Term'], drop_first=True) # for term
df6 = pd.get_dummies(df3['Home Ownership'], drop_first=True) # for Home Ownership
df7 = pd.get_dummies(df3['Purpose'], drop_first=True) # for Purpose

newdf = df3.drop(['Loan Status','Term','Home Ownership','Purpose'],axis = 1)
newdf2 = pd.concat([newdf,df4,df5,df6,df7],axis = 1)
newdf2


# In[9]:


X = newdf2.drop(['Fully Paid','Maximum Open Credit'],axis=1)
X


# In[10]:


Y = newdf2['Fully Paid']
Y


# In[11]:


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.001, random_state = 45)


# In[12]:


# this model is to predict if we get loan or not
model = RandomForestClassifier()
model.fit(X_train,y_train)


# In[13]:


model.score(X_test,y_test)


# In[14]:


pickle.dump(model, open('model_random_forest', 'wb'))


# In[15]:


x = pickle.load(open('model_random_forest','rb'))
x


# In[16]:


# # this model is to predict amount of loan which we can get
# reverse_model = RandomForestClassifier()
# X = newdf2.drop(['Current Loan Amount','Fully Paid'],axis=1)
# Y = newdf2['Current Loan Amount']

# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.001, random_state = 45)
# reverse_model.fit(X_train,y_train)
# reverse_model.score(X_test,y_test)


# In[17]:


X.columns


# In[18]:


len(X.columns)


# In[19]:


df2['Purpose'].unique()


# In[20]:


df2['Home Ownership'].unique()


# In[21]:


# x
# Business loan not there in purpose
# Home Mortgage not there in home ownership
# long term not there in term

# y
# charged off not there in loan Status


# In[ ]:




