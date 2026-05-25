#!/usr/bin/env python
# coding: utf-8

# In[4]:


lists=[23,45,67,34,89]
def AgeCategory():
    for age in lists:
        if (age<18):
            print("Children")
        elif(age<35):
            print("Adult")
        elif(age<59):
            print("Citizen")
        else:
            print("Senior Citizen")


# In[5]:


AgeCategory()


# In[6]:


age=int(input("Enter the age:"))
def AgeCategory():
    if (age<18):
        print("Children")
        cate="Children"
    elif(age<35):
        print("Adult")
        cate="Adult"
    elif(age<59):
        print("Citizen")
        cate="Citizen"
    else:
        print("Senior Citizen")
        cate="Senior Citizen"
    return cate
AgeCategory()
agecate=AgeCategory()


# In[7]:


def oddEven():
    num=int(input("Enter the number:"))
    if((num%2)==0):
        print("Even number")
        msg="even number"
    else:
        print("Odd number")
        msg="even number"
    return msg

oddEven()
function=oddEven()
print(function)


# In[1]:


class multipleFunctions():
    def oddEven():
        num=int(input("Enter the number:"))
        if((num%2)==0):
            print("Even number")
            msg="even number"
        else:
            print("Odd number")
            msg="even number"
        return msg

    def BMI():
        BMI=float(input("Enter the BMI"))
        if(BMI<18.5):
            print("Underweight")
            message="Underweight"
        elif(BMI<24.9):
            print("Normal")
            message="Normal"
        elif(BMI<29.9):
            print("Overweight")
            message="Overweight"
        else:
            print("Obese")
            message="Obese"
        return message

multipleFunctions.BMI()


# In[ ]:




