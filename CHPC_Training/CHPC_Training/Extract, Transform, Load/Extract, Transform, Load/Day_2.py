# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:50:01 2024

@author: climate.intern
"""


#Extract, Transform, Load

import pandas as pd


#Extracting data 

country_df = pd.read_csv("country_data_index.csv", index_col=0)


#Adding column names to data

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

iris_df = pd.read_csv("iris.csv", header=None, names= column_names)


#Adding data with different file types

#Text files

Geospatial_df = pd.read_csv("Geospatial Data.txt",sep=";")

#Excel files

residentdoctors_df = pd.read_excel("residentdoctors.xlsx")

#Json files

student_df = pd.read_json("student_data.json")


Heart_Disease_df = pd.read_csv("https://github.com/abvindi/Heart-Disease-Prediction/blob/main/heart.csv")