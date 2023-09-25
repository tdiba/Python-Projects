#!/usr/bin/env python
# coding: utf-8

# In[8]:


name= input("Please enter your name: ")
weight=(int(input("Please enter your weight in kg: ")))
height=(float(input("Please enter your height in m: ")))
BMI=weight/(height)**2
print(BMI)

if BMI>0:
    if (BMI<18.5):
        print(name + ", you are underweight.")
    elif(BMI<=24.9):
        print(name + ", you are normal weight.")
    elif(BMI<29.9):
        print(name + ", you are overweight.")
    elif(BMI<34.9):
        print(name + ", you are obese.")
    else:
        print(name + ", you are morbidly obese.")
else:
    print("Please enter valid input")


