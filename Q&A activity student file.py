#!/usr/bin/env python
# coding: utf-8

# ## 1. Complete the following code to find the area of an equilateral triangle. Output should be as displayed

# In[10]:


import math
side = float(input("Enter the side of the equilateral triangle: "))
area = ((math.sqrt(3))/4)*pow(side,2)
print(area)


# ## 2. Write a program to count the number of each characters in a string

# In[11]:


str_1 = 'india'
len(str_1)


# ## 3. Write a program to find the area and perimeter of a rectangle using functions

# Area of a rectangle

# In[12]:


def area(l,b):
    a = l*b
    return a
area(3,4)


# Perimeter of a rectangle

# In[13]:


def area(l,b):
    p = 2*(l+b)
    return p
area(3,4)


# ## 4. Write a program to print the fibonacci series till a specified number

# In[14]:


n = int(input('Enter the number :'))
x = 0
y = 1
print(x)
print(y)
for i in range(1,n):
    z = x+y
    x = y
    y = z
    print(z)


# ## 5. Complete the following code to find the minimum of 3 number using conditional statements. Output should be as displayed

# In[3]:


a,b,c = input("Enter three numbers followed by  : ").split()

print("First number :",a)
print("Second number :",b)
print("Third number :",c)
if a == b == c:
    print("Entered numbers are equal!!!")
elif b > a < c :
    print(a," is smallest")
elif a > b < c :
    print(b," is smallest")
elif a > c < b :
    print(c," is smallest")


# ## 6. Write a program to print star pyramind. The number of rows should be taken as input from the user

# In[6]:


num = int(input('enter the number :'))
for i in range(0,num):
    for j in range(0,i+1):
        print('*' ,end = '')
    print()


# ## 7. Complete the following code to convert hour into seconds. Output should be as displayed

# In[8]:


def to_seconds(t):
    t = t * 60 * 60 
    return t
time_in_hours = int(input('Enter  time in Hours:'))
print(time_in_hours ," Hour is equal to" ,to_seconds(time_in_hours) ," Seconds")


# ## 8. Write a program to print multiplication table as below

# In[10]:


num = int(input('Enter a number to find the multiplication table:'))
for i in range(1, 11):
    print(num,"X",i,"=",num * i)


# ## 9. Write a program to take your 5 favorite food as list and print each as 'I like Biriyani'

# In[11]:


list = ['cake','biriyani','noodles','ghee rice','dosa']
for i in list:
    print('I like',i)


# In[ ]:




