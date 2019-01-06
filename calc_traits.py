# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 12:14:57 2019

@author: MY
"""

#%%
import pandas as pd
import json
import os

#%%
with open('q_division.json','r') as f:
    q_division=json.load(f)



#%%

all_files=os.listdir("u_a_json/")

#%%
#with open('u_a_json/1997_012113.txt.json','r') as f:
#    a=json.load(f)

#%%
    
for i in all_files:
    traits={}
    with open(f'u_a_json/{i}','r') as f:
        user=json.load(f)
    
    
    
    
    
    
    
    
    
