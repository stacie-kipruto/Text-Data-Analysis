#!/usr/bin/env python
# coding: utf-8

# # 1. Problem Statement

# ### 1 billion hours of Youtube are watched per day. It is the 2nd most visited site in the world.

# ### YouTube attracts 44% of all internet users whereas 37% of all mobile internet traffic belongs to YouTube

# # 2.SENTIMENTS

# In[1]:


import numpy as np #for numerical data
import pandas as pd #for data manipulation
import matplotlib.pyplot as plt #for vis
import seaborn as sns


# In[2]:


df_comments = pd.read_csv ("GBcomments.xls" , error_bad_lines = False)
df_comments


# In[3]:


df_comments.head(5)


# #### we are now performing sentiment analysis with respect to "comment_text" feature on the above

# #### to do this, we install an external library called textblob library (pip install textblob on conda prompt)

# In[4]:


from textblob import TextBlob


# In[5]:


TextBlob("It's more accurate to call it the M+ (1000) be...").sentiment.polarity


# In[6]:


df_comments.isna().sum() #to get the sum of all missing values


# In[7]:


df_comments.dropna(inplace=True) #to drop all null values


# In[8]:


polarity = []

for i in df_comments ["comment_text"]:
    polarity.append(TextBlob(i).sentiment.polarity)


# In[9]:


df_comments["polarity"] = polarity


# In[10]:


df_comments.head(20)


# # 3. EDA FOR POSITIVE SENTIMENTS

# ### we need positive polarity for this step. Therefore we are going to set the positive polarity as ==1

# ### I am going to create and parse a filter in the data frame

# In[11]:


df_comments_positive = df_comments[df_comments["polarity"] ==1]


# In[12]:


df_comments_positive.shape


# In[13]:


df_comments_positive.head()


# ### to visualize 'comment_text' feature we pip install worldcloud for comments. it is a tool to show how important a word is in a feature

# In[14]:


from wordcloud import WordCloud, STOPWORDS


# In[15]:


stopwords = set(STOPWORDS)


# In[16]:


''.join (df_comments_positive["comment_text"]) #this is the entire data to parse into wordcloud it's a chunk of data


# In[17]:


total_df_comments = ''.join (df_comments_positive["comment_text"])


# In[18]:


wordcloud= WordCloud(width = 1000, height = 500, stopwords = stopwords).generate(total_df_comments)


# In[19]:


plt.figure(figsize = (15,5))
plt.imshow(wordcloud)
plt.axis("off")


# ### from this, we see the most common positive words as "AWESOME, BEST, VIDEO, PERFECT".
# ### The bigger the size of the word, the bigger the polarity it has

# # 4. EDA FOR NEGATIVE SENTIMENTS

# In[20]:


df_comments_negative = df_comments[df_comments["polarity"] ==-1]


# In[21]:


total_df_comments = ''.join (df_comments_negative["comment_text"])


# In[22]:


wordcloud= WordCloud(width = 1000, height = 500, stopwords = stopwords).generate(total_df_comments)


# In[23]:


plt.figure(figsize = (15,5))
plt.imshow(wordcloud)
plt.axis("off")


# # 5. ANALYSING TAGS COLUMN, WHAT ARE THE TRENDING TAGS ON YOUTUBE?

# In[24]:


df_videos = pd.read_csv("USvideos.csv") #when you run, you will come accross a Parse error. To clear this, set a parameter, "error_bad_lines = False"


# In[25]:


df_videos = pd.read_csv("USvideos.csv", error_bad_lines = False)
df_videos


# In[26]:


df_videos.head()


# In[27]:


df_videos["tags"] #to access the tags column


# In[28]:


' '.join(df_videos["tags"]) #to join all the tags, too get a bunch of tags in a string


# In[29]:


tags_complete = ' '.join(df_videos["tags"])
tags_complete


# In[30]:


#there is lots of noise in the above data, we are therefore going to remove it with the fxn below:


# In[31]:


import re #ragular expression module for text data


# In[32]:


#using a substitute fxn to remove special characters except A-Z characters. (^'apart from A-Z', replace with space). All this is in the function TAGS             


# In[33]:


tags = re.sub ('[^a-zA-Z]', ' ', tags_complete)
tags


# In[34]:


tags= re.sub(' + ', ' ', tags)


# In[35]:


wordcloud = WordCloud(width = 1000, height = 500, stopwords = set(STOPWORDS)).generate(tags)


# In[36]:


plt.figure(figsize = (15,5))
plt.imshow(wordcloud)
plt.axis('off')


# # 6. ANALYSIS ON LIKES, VIEWS & DISLIKES: HOW THEY CORRELATE TO EACH OTHER

# ### I'll use a regression plot because i'm trying to find the relationship between two variables. This will be done using seaborn

# In[37]:


sns. regplot(data= df_videos, x="views", y="likes")
plt.title("Regression plot for views & likes")


# In[38]:


sns. regplot(data= df_videos, x="views", y="dislikes")
plt.title("Regression plot for views & dislikes")


# In[39]:


# in the above, when views are increasing, dislikes reduce


# ### using correlation matrix to see how they are correlated

# In[40]:


correlation = df_videos[["views", "likes", "dislikes"]]


# In[41]:


correlation.corr()


# In[42]:


sns.heatmap(correlation.corr(), annot= True)


# # 7. EMOJI ANALYSIS ON COMMENTS

# In[43]:


df_comments.head()


# In[44]:


df_comments["comment_text"][1]


# In[45]:


print("\U0001F600")


# In[46]:


import emoji


# In[47]:


len(df_comments)


# In[48]:


comment = df_comments ['comment_text'][1]


# In[49]:


[c for c in comment if c in emoji.UNICODE_EMOJI]


# In[50]:


emoji.__version__


# In[51]:


str= ' '
for i in df_comments ["comment_text"]:
    list = [c for c in i if c in emoji.UNICODE_EMOJI]
    for ele in list:
        str=str+ele


# In[52]:


len(str)


# In[53]:


#str will print all the emojis in the youtube text we're analysing 'this is supposed to be a code but it makes the machine hang'


# In[54]:


result = {}
for i in set(str):
    result[i]=str.count(i) #to return a value associated with i,


# In[55]:


result


# In[56]:


result.items()


# In[57]:


final={} #to create a dictionary for storing the data

for key, value in sorted(result.items(), key= lambda item:item[1]):
    final[key]=value


# In[58]:


final


# In[59]:


keys = [*final.keys()]


# In[60]:


keys


# In[61]:


values= [*final.values()]


# In[62]:


values


# In[63]:


df=pd.DataFrame({"chars":keys[-20:], "num":values[-20:]}) #parsing data into a data frame with the last 20 entries


# In[64]:


df


# In[65]:


import plotly


# In[66]:


import plotly.graph_objs as go
from plotly.offline import iplot #for visualizations in jupyter


# In[67]:


trace= go.Bar(
x=df["chars"],
y=df["num"]
)

iplot([trace])


# In[ ]:




