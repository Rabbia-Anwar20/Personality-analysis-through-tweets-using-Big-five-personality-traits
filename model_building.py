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
#print(X)
y=labels

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

#%%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

#%% apply xgboost
import xgboost as xgb
xgb_regr=xgb.XGBRegressor(max_depth=3,n_estimators=300,learning_rate=0.05).fit(X_train,y_train)
predictions=xgb_regr.predict(X_test)

#%% apply randomforest
from sklearn.ensemble import RandomForestRegressor
rf=RandomForestRegressor(n_estimators=10,random_state=42)
rf.fit(X_train,y_train)
pred=rf.predict(X_test)
#%%
print(44)

#%% linear regression
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X_train,y_train)
pred=lr.predict(X_test)
#print(lr.score(X_test,y_test))

#%% check accuracy
from sklearn.metrics import r2_score
print(r2_score(y_test,pred))

