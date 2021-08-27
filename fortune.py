#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 22:31:17 2021

@author: tansha
"""
#importing important libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# to read the csv file
data = pd.read_csv('fortune.csv')       

#to calculate the average revenue 
avg_revenue = data['Revenues($M)'].mean()   

#to calculate the average profit      
avg_profit = data['Profits($M)'].mean()     

fig, ax = plt.subplots(figsize = (12,6))
w = 0.25

#to create simple horizontal bar plots
ax.barh(np.arange(10)+w , data['Profits($M)'], color = '#80E8BC', label = 'Profits($M)', height = w)
ax.barh(np.arange(10)-w, data['Revenues($M)'],  color = '#017A2A', align = 'edge', label = 'Revenues($M)', height = w)

#to create vertical lines for average revenue and average profits
ax.axvline(avg_revenue, color = '#0D26B5', ls = '--')
ax.axvline(avg_profit, color = '#B50D3F', ls = '--')

#editing the ylabels
ax.set_yticks(np.arange(10))
ax.set_yticklabels(['Toyota Motor', 'Amazon', 'BP', 'Volkswagen', 'Saudi Aramaco', 'Royal Dutch Shell', 'China National Petroleum', 'State Grid', 'Sinopec Group', 'Walmart'], weight = 'medium', fontsize = 14)
col = ['#01693D','#01693D','#01693D','#01693D' ,'#B50D3F' ,'#0D26B5', '#0D26B5', '#0D26B5', '#0D26B5', '#0D26B5'  ]
for ticklabel, tickcolor in zip(plt.gca().get_yticklabels(), col):
    ticklabel.set_color(tickcolor)
    
#adjusting the title
ax.set_title('Top 10 Fortune GLOBAL500 Companies', weight = 'bold', x = 0, y = 1.2, fontsize = 16)

#editing the xlabels
ax.set_xlabel('Numbers in Millions', loc = 'left', color = '#01401F', weight = 'semibold', fontsize = 12)
ax.text(x = -60000, y = 10.3,s = 'Companies', color = '#01401F', weight = 'semibold', fontsize = 12)

#labelling the average revenue and average profit vertical lines 
ax.text(x = 20000, y = 9.2, s = 'Average Profit ($18839.25M)', color = '#B50D3F')
ax.text(x = 352000, y = 9.2, s = 'Average Revenue ($349705.5M)', color = '#0D26B5')

#editing the textboxes
props_2 = dict(boxstyle='round', facecolor='#D1EBF0', alpha=0.5)
props_1 = dict(boxstyle='round', facecolor='#F0D1EB', alpha=0.5)
props_3 = dict(boxstyle='round', facecolor='#E6F0D1', alpha=0.5)
ax.text(x = 400000, y = 3.5, s = 'Only Saudi Aramaco had\nabove average profits', color = '#B50D3F', weight = 'semibold', bbox = props_1)
ax.text(x = 400000, y = 6, s = 'Royal Dutch Shell, China National Petroleum,\nState Grid, Sinopec Group and Walmart\n had above average revenues', color = '#0D26B5', weight = 'semibold', bbox = props_2)
ax.text(x = 400000, y = 1.2, s = 'Volkswagen, BP, Amazon and Toyota Motor\nhad below average revenues and profits', color = '#01693D', weight = 'semibold', bbox = props_3)

#removing unwanted axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

#removing the short ticks
ax.tick_params(bottom = False, left = False)
plt.legend(ncol = 2, loc = (0.2,1.1))
plt.show()
