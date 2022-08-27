#!/usr/bin/env python
# coding: utf-8

# # Problem 1: Basic approach

# In[ ]:


def prime_num(N):
  '''integers below or equal to one are out of scope 
  for the definition of prime numbers.'''

  if(N<=1):
    return False
   
  #using most basic algorithm
  for i in range(2,N):
    #if divisible by i, then n is not a prime number.
    if(N%i==0):
      return False
   
  #otherwise, N is prime number.
  return True


# In[ ]:


import time

st = time.time()
# num = int(input("Input the value of N:"  ));
num = 500
#checking for all number: 1 to num
for i in range(1,num+1):
  #if i is prime
  if(prime_num(i)):
    print(i)
et = time.time()
print(et-st)
    # print(i ,end=" ")


# # Problem 1: Decreasing number of iterations (more efficient approach)

# In[ ]:


def prime_num(N):
  '''integers below or equal to one are out of scope 
  for the definition of prime numbers.'''

  if(N<=1):
    return False
   
  #using improved basic algorithm
  for i in range(2,int(N//2)+1):
    #if divisible by i, then n is not a prime number.
    if(N%i==0):
      return False
   
  #otherwise, N is prime number.
  return True


# In[ ]:


import time

st = time.time()
# num = int(input("Input the value of N:"  ));
num = 500
#checking for all number: 1 to num
for i in range(1,num+1):
  #if i is prime
  if(prime_num(i)):
    print(i)
et = time.time()
print(et-st)
    # print(i ,end=" ")


# # Problem 1: Eratosthenes algorithm (even more efficient approach)

# In[ ]:


def prime_num(N):
  '''integers below or equal to one are out of scope 
  for the definition of prime numbers.'''

  if(N<=1):
    return False
   
  #using Eratosthenes algorithm
  for i in range(2,int(N**(1/2))+1):
    #if divisible by i, then n is not a prime number.
    if(N%i==0):
      return False
   
  #otherwise, N is prime number.
  return True


# In[ ]:


import time

st = time.time()
# num = int(input("Input the value of N:"  ));
num = 500
#checking for all number: 1 to num
for i in range(1,num+1):
  #if i is prime
  if(prime_num(i)):
    print(i)
et = time.time()
print(et-st)
    # print(i ,end=" ")


# In[ ]:





# # Problem 2

# In[ ]:


def exponent(x, y):
     
    if y == 0:
        return 1
    if y % 2 == 0:
        return exponent(x, y // 2) * exponent(x, y // 2)
         
    return x * exponent(x, y // 2) * exponent(x, y // 2)
##
## We can also use an inbuilt function for exponent(x, y), i.e. pow(x, y): students should try it.
##
def CubicSumDigits(num):
    if type(num)!=int or num<0:
        return print('!!! Please Provide a valid integer')
    cube_sum_digits = 0

    while num > 0:
        mod = num%10
        cube_sum_digits = cube_sum_digits + exponent(mod, 3)
        num = num//10

    return cube_sum_digits

CubicSumDigits(370)


# # Problem 3: Extension of Problem 2.

# In[ ]:


def len_num(num):
 
    # Variable to store of the number
    n = 0
    while (num != 0):
        n = n + 1
        num = num // 10
         
    return n

def LenExpoSumDigits(num):
    if type(num)!=int or num<0:
        return print('!!! Please Provide a valid integer')
    cube_sum_digits = 0
    length_num = len_num(num)
    n = num
    while n > 0:
        mod = n%10
        cube_sum_digits = cube_sum_digits + exponent(mod, length_num)
        n = n//10

    return (print(cube_sum_digits), print('Is {} an Armstrong number?'.format(num), cube_sum_digits == num))

LenExpoSumDigits(12) ## 0, 1, 153, 370, 371, 407, 1634, 8208, 9474 etc.


# # Problem 4: Counting zeros in n!

# In[ ]:


def ZerosInFact(num):
    if num<5 and num>=0:
        return 0
    elif type(num)!=int or num<0:
        return ('!!! Please Provide a valid integer')
    count = 0
    while num>=5:
        num = int(num/5) ## or n//5
        count = count + num
    return count

print(ZerosInFact(-2))
# print(ZerosInFact(4))
# print(ZerosInFact(5))
# print(ZerosInFact(10))
# print(ZerosInFact(100))


# # Problem 5: Number of days in February

# In[ ]:


def leap_noleap(n):    
    # no_of_days_noleap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # no_of_days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    feb_no_of_days = None

    if type(n)!=int or n<0:
        return ('!!! Please provide a valid year')
    
    if (n%4 == 0 and n%100 != 0) or (n%400==0):
        feb_no_of_days = 29
    else:
        feb_no_of_days = 28
    return ('This year has {} days in February'.format(feb_no_of_days))

leap_noleap(2100)


# In[ ]:


count_leap = 0
count_noleap = 0
for i in range (1896, 2400):
    print (i,':', leap_noleap(i))
    if leap_noleap(i) == 'This year has 29 days in February':
        count_leap +=1
    if leap_noleap(i) == 'This year has 28 days in February':
        count_noleap +=1
print('number of leap years between 1896-2399:', count_leap, 'number of no-leap years between 1896-2399:', count_noleap)


# In[ ]:





# <a style='text-decoration:none;line-height:16px;display:flex;color:#5B5B62;padding:10px;justify-content:end;' href='https://deepnote.com?utm_source=created-in-deepnote-cell&projectId=4cf8407e-fc91-4c63-a914-f358932163f4' target="_blank">
# <img alt='Created in deepnote.com' style='display:inline;max-height:16px;margin:0px;margin-right:7.5px;' src='data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iODBweCIgaGVpZ2h0PSI4MHB4IiB2aWV3Qm94PSIwIDAgODAgODAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDU0LjEgKDc2NDkwKSAtIGh0dHBzOi8vc2tldGNoYXBwLmNvbSAtLT4KICAgIDx0aXRsZT5Hcm91cCAzPC90aXRsZT4KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPgogICAgPGcgaWQ9IkxhbmRpbmciIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJBcnRib2FyZCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEyMzUuMDAwMDAwLCAtNzkuMDAwMDAwKSI+CiAgICAgICAgICAgIDxnIGlkPSJHcm91cC0zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjM1LjAwMDAwMCwgNzkuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBpZD0iUGF0aC0yMCIgZmlsbD0iIzAyNjVCNCIgcG9pbnRzPSIyLjM3NjIzNzYyIDgwIDM4LjA0NzY2NjcgODAgNTcuODIxNzgyMiA3My44MDU3NTkyIDU3LjgyMTc4MjIgMzIuNzU5MjczOSAzOS4xNDAyMjc4IDMxLjY4MzE2ODMiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0zNS4wMDc3MTgsODAgQzQyLjkwNjIwMDcsNzYuNDU0OTM1OCA0Ny41NjQ5MTY3LDcxLjU0MjI2NzEgNDguOTgzODY2LDY1LjI2MTk5MzkgQzUxLjExMjI4OTksNTUuODQxNTg0MiA0MS42NzcxNzk1LDQ5LjIxMjIyODQgMjUuNjIzOTg0Niw0OS4yMTIyMjg0IEMyNS40ODQ5Mjg5LDQ5LjEyNjg0NDggMjkuODI2MTI5Niw0My4yODM4MjQ4IDM4LjY0NzU4NjksMzEuNjgzMTY4MyBMNzIuODcxMjg3MSwzMi41NTQ0MjUgTDY1LjI4MDk3Myw2Ny42NzYzNDIxIEw1MS4xMTIyODk5LDc3LjM3NjE0NCBMMzUuMDA3NzE4LDgwIFoiIGlkPSJQYXRoLTIyIiBmaWxsPSIjMDAyODY4Ij48L3BhdGg+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNMCwzNy43MzA0NDA1IEwyNy4xMTQ1MzcsMC4yNTcxMTE0MzYgQzYyLjM3MTUxMjMsLTEuOTkwNzE3MDEgODAsMTAuNTAwMzkyNyA4MCwzNy43MzA0NDA1IEM4MCw2NC45NjA0ODgyIDY0Ljc3NjUwMzgsNzkuMDUwMzQxNCAzNC4zMjk1MTEzLDgwIEM0Ny4wNTUzNDg5LDc3LjU2NzA4MDggNTMuNDE4MjY3Nyw3MC4zMTM2MTAzIDUzLjQxODI2NzcsNTguMjM5NTg4NSBDNTMuNDE4MjY3Nyw0MC4xMjg1NTU3IDM2LjMwMzk1NDQsMzcuNzMwNDQwNSAyNS4yMjc0MTcsMzcuNzMwNDQwNSBDMTcuODQzMDU4NiwzNy43MzA0NDA1IDkuNDMzOTE5NjYsMzcuNzMwNDQwNSAwLDM3LjczMDQ0MDUgWiIgaWQ9IlBhdGgtMTkiIGZpbGw9IiMzNzkzRUYiPjwvcGF0aD4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+' > </img>
# Created in <span style='font-weight:600;margin-left:4px;'>Deepnote</span></a>
