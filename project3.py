# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:14:57 2018

@author: ndtetteh
"""

import pandas as pd
import json
import matplotlib.pyplot as plt


db = json.load(open('./smallerDataSet.json'))
nutrients = pd.DataFrame(db[0]['nutrients'])
info_keys = ['description', 'group', 'id', 'manufacturer']
info = pd.DataFrame(db, columns=info_keys)

nutrients = []
for rec in db:
    fnuts = pd.DataFrame(rec['nutrients'])
    fnuts['id'] = rec['id']
    nutrients.append(fnuts)
nutrients = pd.concat(nutrients, ignore_index=True)

#removing duplicates
nutrients = nutrients.drop_duplicates()

#rename  and apply to info dataframe
col_mapping = {'description' : 'food',
               'group' : 'fgroup'}
info = info.rename(columns=col_mapping, copy=False)

nut_col_mapping = {'description' : 'nutrient',
               'group' : 'nutgroup'}

nutrients = nutrients.rename(columns=nut_col_mapping, copy=False)

#merging data
ndata = pd.merge(nutrients, info, on='id', how='outer')


''''
4.   For the ‘Amino Acids’ nutrient group output a table showing 
    the different constituents of the group (Alanine, Glycine, Histidine etc) 
    and the foods in which they are present (Gelatins, dry powder, beluga, meat...etc)
'''
by_nutrient = ndata.groupby(['nutgroup', 'nutrient'])
get_maximum = lambda x: x.xs(x.value.idxmax())
get_minimum = lambda x: x.xs(x.value.idxmin())
max_foods = by_nutrient.apply(get_maximum)[['value', 'food']]
# make the food a little smaller
max_foods.food = max_foods.food.str[:50]

#Amino Acid tabel
#max_foods.loc['Amino Acids']['food']
max_foods.loc['Amino Acids']


'''
5.   For all the different nutrient group (beef Products, Pork 
    Products, dairy and egg products etc.) calculate the median Zinc content
     (median of the zinc content in all the foods that constitute the nutrient group)
     
6.   Plot the distribution of median Zinc Content for different nutrient groups as a bar chart.
'''
result = ndata.groupby(['nutrient', 'fgroup'])['value'].quantile(0.5)
plt.figure(figsize=[16,10])
result['Zinc, Zn'].plot(kind='barh', title = "Distribution of Median Zinc Content for Different Nutrient Groups")
plt.xlabel("Zinc Content")
plt.show()


