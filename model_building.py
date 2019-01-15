# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 08:57:04 2019

@author: MY
"""

#%%
import pandas as pd


#%%
data=pd.read_csv('traits_essays.csv',encoding='latin1')
data.head()
#%%
#labels=data[['Extraversion','Agreeableness','Conscientiousness','Neuroticism','Openness']]
labels=data.iloc[:,-5:]
tweets=data.iloc[:,1]

#%%
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=TfidfVectorizer()
X=vectorizer.fit_transform(tweets)
print(X)

#%% TFIDF prac
from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
     'This is the first document.',
     'This document is the second document.',
     'And this is the third one.',
     'Is this the first document?',
]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(X.shape)
