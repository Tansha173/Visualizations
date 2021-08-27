#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 22:48:08 2021

@author: tansha
"""

#importing important libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# to read the csv file
cars = pd.read_csv('cars_data.csv')

#calculating average number of cars sold each month for two years
lst = []
for i in range(len(cars['month'])):
    lst.append((cars['2018'][i] + cars['2019'][i]) / 2)
cars['avg'] = lst 

fig, ax = plt.subplots(figsize = (12,5))

#line plot for 2018, 2019 and average data
ax.plot(cars['month'], cars['2018'], color = '#510051', lw = 2)
ax.plot(cars['month'], cars['2019'], color = '#751975', lw = 0.8)
ax.plot(cars['month'], cars['avg'], color = '#d1b2d1', lw = 0.6, ls = '-.')

#adjusting the title
ax.set_title('Monthly vehicles sold trend', fontsize = 18, fontweight = 'bold', x = 0, y = 1.2, color = '#3D003D')

#adjusting the subtitle
ax.text(x = -3, y = 113, s = 'Years 2018 and 2019', weight = 'medium', fontsize = 14, color = '#3D003D')

#adjusting the xlabels
plt.xticks(np.arange(12))
ax.set_xlabel('Months', loc = 'left', fontsize = 12, weight = 'semibold', color = '#42325b')
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], color = '#3D003D')

#adjusting the ylabel
ax.set_ylabel('Number of cars', loc = 'top', fontsize = 12, weight = 'semibold', color = '#42325b')

#annotating the lineplots
ax.text(x = 11.1, y = 86, s = '2018', color = '#510051', weight = 'semibold')
ax.text(x = 11.1, y = 40, s = '2019', color = '#751975', weight = 'semibold')
ax.text(x = 11.1, y = 63, s = 'Average', color = '#d1b2d1', weight = 'semibold')

#highlighting the data point 
ax.text(x = 12, y = 70, s = 'The dot highlights the data point\nbeyond which 2018 sales rise up\nand 2019 sales drop', color = 'maroon', weight = 'medium')
plt.plot(8.5, 58.5, marker = 'o', markersize = 10, color = 'maroon')
plt.arrow(x = 12, y = 70, dx = -3.1, dy = -11, width = 0.1, color = '#000000')

#removing the short ticks
ax.tick_params(left = False, bottom = False)
ax.set_facecolor('#ffffff')

#removing the unwanted axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()