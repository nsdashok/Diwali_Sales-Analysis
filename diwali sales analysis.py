#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # for visulazations data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns # for any types of graph


# In[2]:


# To read the csv file we have to upload the file first in jupyter than we will read from these codes.  
df=pd.read_csv('diwalisaledata.csv',encoding="unicode_escape") # here i am using encoding that if file contain characters from different languages or non-standard character sets.


# In[3]:


# this shape function will give us that how many Row and Columns we have in this data, (Rows, Columns)
df.shape


# In[4]:


# this head function will give us First five record along with the Header, and if we want view more than we can specify that how many rows we have to see in display. like df.head(12)
df.head(10)


# In[5]:


# describe function will return us the statical and mathematic imputation mention below like mean, count, std, min, max, % 
df.describe()


# In[6]:


# info function will return us the total number of columns and is this null value persent or not and Data Type
df.info()


# In[7]:


# here Drop function will delete the column and columns should be square braket and here inplace=True will save the changes if we will inplace True than changes will not saved. other wise for saving change we have to make another file. us new_file_name= 
df.drop(['Status','unnamed1'], axis=1, inplace=True)


# In[8]:


# check in head end of columns there is not columns named stauts and unnamed1
df.head()


# In[9]:


# i am checking the shape again to verify that i removed 2 columns and saved it so ... yes i can see the 2 columns have gone.
df.shape


# In[10]:


# i can also check here removed columns is not here
df.info()


# In[11]:


# here isnull function giving us that how many null value and where null value persent in the data
pd.isnull(df).sum()


# In[12]:


# ok now you can see these is many false here it means wherever we can see false therse is no null value. if we see Ture it means there is null values
df.isnull()


# In[13]:


# you you can see... innext step i will be droping null values and i will inplace this.
df.isnull().sum()


# In[14]:


# this function will drop the null value form data.
df.dropna(inplace=True)


# In[15]:


# now you can the null value droped .
df.shape


# In[16]:


# and in sum of null value there is zero null value in every columns
df.isnull().sum()


# In[17]:


# this is a example to understanding of null value, i have left a row with city value so its showing None:
data_test=[['madhav','Kumar', 11, 'Gurgaon'],['Ashok','Saw', 32, 'Delhi'],['Nitu','Kumari', 21, 'Mumbai'],['Diyu','Kumar',6,]]
df_test=pd.DataFrame(data_test,columns=['First_Name','Second_Name','Age','City'])
df_test


# In[ ]:





# In[ ]:





# In[ ]:





# In[18]:


# Here i am changing the data type of amount from float to Integer 
df['Amount']=df['Amount'].astype('int')


# In[19]:


# now i am verifying that yes changes have changed or not 
df['Amount'].dtypes


# In[20]:


df.columns


# In[21]:


# now i am changing or renaming the column Name like marital status to shadi shuda. 
df.rename(columns={'Marital_Status': 'shadi_suda'})


# In[22]:


# now here if we need to do mathmetical imputation to 1 column or 2 column and what so ever it wil give you describe... 
df[['Age','Orders','Amount']].describe()


# df.columns

# In[30]:


# from here i am going to build any graph, here its countplot graph on the basis of gender and also put value use for loop
ax=sns.countplot(x='Gender',data=df) # here sns comes from imported library seaborn as sns
for bars in ax.containers:
    ax.bar_label(bars)


# # Exploratory Data Analysis
# 

# ### now we are going to do the analysis regarding sale firstly we will check that which gender have spend more amount...

# ## Gender wise

# In[31]:


# here i made a sales_gen to and will see in graph
sale_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Gender',y='Amount', data=sale_gen)


# In[32]:


df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)


# In[33]:


sales_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Gender',y='Amount', data=sales_gen)


# In[27]:





# ### From above graph we can see that most of the buyer are female and even purchasing power of female is gretar than man

# ## Age wise

# In[34]:


df.columns


# In[39]:


# here we are applying by age group and see that which age group have the more purchasing power so we can do the more analysis on that age group
ax=sns.countplot(x='Age Group',data=df)


# #### here we can see the age group of 26-35 having more purchasing power than others age group

# In[40]:


# now what i am doing that i am using hue.. what it will be doing that convert the damost shopping ta in Gender basis that in which group male or female having 
ax=sns.countplot(x='Age Group',data=df, hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[42]:


# now its showing sales according to age group sorted of sum of amount with a bar graph 
sales_gen=df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending = False)
sns.barplot(x='Age Group', y='Amount', data=sales_gen)


# ### from above graphs we can see that most of the buyers form 26-35 age of group and as per above gram female is more than male

# ## State wise

# In[58]:


# ok now what i am doing that i want to see that which state having maximum capacity of purchasing and this i want to see the value with order not with  amount 
sales_state=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(12) # here i have used .head to display the number of state we can change the no of state value in head()
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state,x='State',y='Orders')


# In[60]:


# now most order and amount value its possible that less order can spend more amount and vise-varsa
sales_state=df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state, x='State', y='Amount')


# #####  From above graphs we can see that most of the order form UP, MH and KA but total sale /amount is from UP, KA than MH
# 
# 
# here we have the analysy as per state and amount spend

# ## Marital Status wise

# In[68]:


ax=sns.countplot(data=df,x='Marital_Status')
sns.set(rc={'figure.figsize':(4,4)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[69]:


# checking with Marital status spend amount camparing to male and female
sales_state=df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data=sales_state, x='Marital_Status',y='Amount', hue='Gender')


# In[70]:


df.head()


# ### Occupation wise

# In[80]:


# here also doing same with diffrent columns
sns.set(rc={'figure.figsize':(20,5)})
ax=sns.countplot(data=df,x='Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[81]:


sales_Occupation=df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_Occupation, x='Occupation', y='Amount')

for bars in ax.containers:
    ax.bar_label(bars)


# ##### here the most amount spend by It sector and healthcare and aviation ans so on...

# ### Product_Category 

# In[ ]:





# In[88]:


sns.set(rc={'figure.figsize':(20,7)})
ax=sns.countplot(data=df,x='Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[96]:


sales_Product_Category=df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(30,8)})
sns.barplot(data=sales_Product_Category, x='Product_Category', y='Amount')


# #### now here most product catogary sold is food, cloths and so on...

# In[97]:


sales_Product_ID=df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(30,8)})
sns.barplot(data=sales_Product_ID, x='Product_ID', y='Orders')


# In[98]:


fig1, ax1=plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# ## Conclusion of the Diwali sale as per my understanding 

# #### Married women age group 26-35 years from UP, Maharastra and Karnataka working in IT, Healthcare and aviation  are most likly buy products from Cloths, food and Electronic items

# In[99]:


print("Thankyou")


# In[ ]:




