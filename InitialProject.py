#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 13:51:10 2020

@author: password1234
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.style as style
import scipy.stats as stats
import seaborn as sns
style.use('bmh') ## style for charts

from pandas.plotting import scatter_matrix

header_names = [
    'age',
    'class_worker',
    'det_ind_code',
    'det_occ_code',
    'education',
    'wage_per_hour',
    'hs_college',
    'marital_stat',
    'major_ind_code',
    'major_occ_code',
    'race',
    'hisp_origin',
    'sex',
    'union_member',
    'unemp_reason',
    'full_or_part_emp',
    'capital_gains',
    'capital_losses',
    'stock_dividends',
    'tax_filer_stat',
    'region_prev_res',
    'state_prev_res',
    'det_hh_fam_stat',
    'det_hh_summ',
    'instance_weight', ## this field is not used as a feature
    'mig_chg_msa',
    'mig_chg_reg',
    'mig_move_reg',
    'mig_same',
    'mig_prev_sunbelt',
    'num_emp',
    'fam_under_18',
    'country_father',
    'country_mother',
    'country_self',
    'citizenship',
    'own_or_self',
    'vet_question',
    'vet_benefits',
    'weeks_worked',
    'year',
    'income_50k',
]

df = pd.read_csv('/Users/password1234/Documents/Machine Learning/census-income.data.csv', header = None, names = header_names)
df_test = pd.read_csv('/Users/password1234/Documents/Machine Learning/census-income.test.csv', header = None, names = header_names)
df = pd.concat([df, df_test]) #The test file, labeled so it can be merged with original 
df.drop(columns = ['instance_weight'])
df.shape

categorical_features = [
    'class_worker',
    'det_ind_code',
    'det_occ_code',
    'education',
    'hs_college',
    'marital_stat',
    'major_ind_code',
    'major_occ_code',
    'race',
    'hisp_origin',
    'sex',
    'union_member',
    'unemp_reason',
    'full_or_part_emp',
    'tax_filer_stat',
    'region_prev_res',
    'state_prev_res',
    'det_hh_fam_stat',
    'det_hh_summ',
    'mig_chg_msa',
    'mig_chg_reg',
    'mig_move_reg',
    'mig_same',
    'mig_prev_sunbelt',
    'fam_under_18',
    'country_father',
    'country_mother',
    'country_self',
    'citizenship',
    'own_or_self',
    'vet_question',
    'vet_benefits',
    'year',
]
continuous_features = [
    'age', 
    'wage_per_hour',
    'capital_gains',
    'capital_losses',
    'stock_dividends',
    'num_emp',
    'weeks_worked',
  ]
df[categorical_features] = df[categorical_features].astype('category')

df.info()
df.describe()

df.describe(include = 'category')

df.median('age')

df.head()
df.median()

df[categorical_features].describe()

df.groupby(by = 'age').median()
df['age'].mean()

df.boxplot()

#looking at individual boxplots for each feature
vars_to_plot_seperate = [['income_50k','vet_benefits','tax_filer_stat'],
['age'],
['stock_dividends'],
['wage_per_hour'] ]
plt.figure(figsize = (10,6))

for index, plot_vars in enumerate(vars_to_plot_seperate):
    plt.subplot(len(vars_to_plot_seperate)/2,
                2,
                index + 1)
    ax = df.boxplot(column=plot_vars)

plt.show()

ax = scatter_matrix(df, figsize = (15,10))

#Seaborn correlation matrix
cmap = sns.diverging_palette(220, 10, as_cmap =True) #One of the many color mapping

sns.set(style="darkgrid") 
f, ax = plt.subplots(figsize = (9,9))

sns.heatmap(df.corr(), cmap = cmap, annot=True)
f.tight_layout()

#Violin Plots age
f, ax = plt.subplots(figsize = (9,9))

sns.violinplot(x= 'weeks_worked', y = 'age', hue = 'income_50k', data = df,
               split = True, inner = 'quart')

#Violin Plots dividends with age
f, ax = plt.subplots(figsize = (9,9))

sns.violinplot(x= 'stock_dividends', y = 'age', hue = 'income_50k', data = df,
               split = True, inner = 'quart')