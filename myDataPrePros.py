# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 12:02:38 2018

@author: DaffodilPC
"""
import numpy as mp
import matplotlib.pyplot as plot
import pandas as pn

dataset = pd.read_csv("F:/Machine Learning A-Z Template/Part 1 - Data Preprocessing/Data.csv")
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values
