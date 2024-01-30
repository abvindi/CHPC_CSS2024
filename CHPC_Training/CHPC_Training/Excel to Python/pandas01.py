# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:54:07 2024

@author: climate.intern
"""

#Reading In Files With Pandas

import pandas


country_file = pandas.read_csv("country_data.csv")
print(country_file)


diab_file = pandas.read_csv("diab_data.csv")
print(diab_file)

print(diab_file.info())
print(diab_file.describe())




housing_file = pandas.read_csv("housing_data.csv")
print(housing_file)



insurance_file = pandas.read_csv("insurance_data.csv",skiprows=(5))
print(insurance_file)

# Storing Data
B1 = 30
B2 = 40
B3 = 30
B4 = 49

print(B1)
print(B2)


# Using Lists
age = [30,40,30,49,22,35,22,46,29,25,39]
print(age)

# Lists indexes start at 0 which has the value of 30
print(age[0])
print(age[1])
print(age[10])

# This will give an error as there is no value at index 11
print(age[7])


# Basic Stats
age = [30,40,30,49,22,35,22,46,29,25,39]

print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)


country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]

print(country)
print(country[0])
print(country[5])


# Data Storage With Lists
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list) 
print(my_list[:])

my_list.append("pi")
print(my_list)

my_list.insert(1,"pi2")
print(my_list)

my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)
print(len(my_list))

# View a certain range of items:
print(my_list[0:3])




#Dictionaries

person = {'name': 'John Doe', 'age': 30, 'address': '123 Main St.'}
print(person['name'])
