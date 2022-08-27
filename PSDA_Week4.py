#!/usr/bin/env python
# coding: utf-8

# # Problem 1: Convert all the digits of a number to the respective words.

# In[ ]:


def DigitToWord(digit_num):
 
    
    if type(digit_num)!=int:
        return '!!!Provide a valid input'
    # base case
    elif (digit_num == 0):
        return 'Zero'

    

    n = digit_num % 10
    digit_num = digit_num // 10
    
    # print(n)     ### this print before the recurrsion call stacks up numbers from first to last
    # Recurrsion
    DigitToWord(digit_num)


    
    # printing the digits form the string array storing name of the given index
    word_lst = [ "zero", "one", "two", "three", "four",
                "five", "six", "seven", "eight", "nine" ]
    # print (n)     ### this print after the recurrsion call stacks up numbers from last to first
    print(word_lst[n] , end = " ")   ### thats why we don't need to rearrange the numbers before printing.     

# digit_num = int(input('input the desired number: '))
digit_num = 9123450
DigitToWord(digit_num)


# # Problem 2: Converting a dictionary with values as a list to flat dictionary.  

# In[ ]:


def leap_noleap(n):    
    # no_of_days_noleap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # no_of_days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if type(n)!=int or n<0:
        return ('!!! Please provide a valid year')
    
    elif (n%4 == 0 and n%100 != 0) or (n%400==0):
        return 'leap'
    else:
        return 'no-leap'


# In[ ]:


leap_noleap(2400)


# In[ ]:


def no_of_days(year):

    dict_month_days = {'Non-leap no. of days' : [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
                'Leap no. of days' : [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
                'name' : ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'Nov', 'DEC']}
    
    # Convert key-values list to flat dictionary using dict() and zip() functions.
    if leap_noleap(year) == 'leap':
        res = dict(zip(dict_month_days['name'], dict_month_days['Leap no. of days']))
    elif leap_noleap(year) == 'no-leap':
        res = dict(zip(dict_month_days['name'], dict_month_days['Non-leap no. of days']))
    else:
        return leap_noleap(year)
    
    # printing result
    return res


# In[ ]:


[int(i) for i in range(2000, 2101)]


# In[ ]:


no_of_days(2000).items()


# In[ ]:


import sys
from sys import getsizeof
year = [int(i) for i in range(2000, 2101)]
# key_val_list = [(i, j) for i, j in no_of_days(year).items()]

year_days = {}
year_days['leap'] = {}
year_days['no-leap'] = {}
for i in year:
    if leap_noleap(i) == 'leap':
        year_days['leap'][i] = [(key, val) for key, val in no_of_days(i).items()]       
    elif leap_noleap(i) == 'no-leap':
        year_days['no-leap'][i] = [(key, val) for key, val in no_of_days(i).items()]
    else:
        print('!!! Please provide a valid year')
year_days
# sys.getsizeof(year_days)
# local_vars = list(year_days.items())
# for var, obj in local_vars:
#     print(var, sys.getsizeof(obj))


# In[ ]:


len(year_days)


# In[ ]:


year = [int(i) for i in range(2000, 2101)]
# key_val_list = [(i, j) for i, j in no_of_days(year).items()]

year_days = {}
year_days['leap'] = {}
year_days['no-leap'] = {}
leap_year_lst = []
noleap_year_lst = [] 
for i in year:
    if leap_noleap(i) == 'leap':
        leap_year_lst.append(i)       
    elif leap_noleap(i) == 'no-leap':
        noleap_year_lst.append(i)
    else:
        print('!!! Please provide a valid year')
year_days['leap'][tuple(leap_year_lst)] = [(key, val) for key, val in no_of_days(2000).items()]
year_days['no-leap'][tuple(noleap_year_lst)] = [(key, val) for key, val in no_of_days(2100).items()]
# for i in year:
#     year_days[i] = [(key, val) for key, val in no_of_days(i).items()]

year_days
# sys.getsizeof(year_days)
# sys.getsizeof(list(year_days['leap'].keys()))
# local_vars = list(year_days.items())
# for var, obj in local_vars:
#     print(var, sys.getsizeof(obj))


# In[ ]:


year_days


# # Problem 3: Standard deviation of the numeric values in a tuple of the form (('str1',num1),('str2',num2)..so on) 

# In[ ]:


def tup_to_dict(tup):
    ### tuple should be of the form (('a', 5), ('b', 9), ('c', 14) ......)
    return dict(tup)



def sum_val(tup):
    Dict = tup_to_dict(tup)
    return sum(Dict.values())

tup = (('a', 5), ('b', 9), ('c', 14), ('d', 35), ('e', 12), ('f', 43), ('g', 22), ('h', 29), ('i', 13), ('j', 41))
print(sum_val(tup))


# In[ ]:


def sum_tup(tup):
    summ = 0 
    for i in tup:
        summ = summ + i[1]
    return summ


sum_tup(tup)


# In[ ]:


import math
def tup_to_dict(tup):
    ### tuple should be of the form (('a', 5), ('b', 9), ('c', 14) ......)
    return dict(tup)



def std_val(tup):
    Dict = tup_to_dict(tup)
    summ =  sum(Dict.values())
    average = summ/len(Dict)

    std = 0
    for i in Dict.values():
        std = std +  (i - average)**2
    return math.sqrt(std/(len(Dict)-1))

tup = (('a', 5), ('b', 9), ('c', 14), ('d', 35), ('e', 12), ('f', 43), ('g', 22), ('h', 29), ('i', 13), ('j', 41))
print(std_val(tup))


# In[ ]:


def std_tup(tup):
    avg = 0
    std = 0 
    for i in tup:
        avg = avg + i[1]
    avg = avg/len(tup)
    for i in tup:
        std = std +  (i[1] - avg)**2
    return math.sqrt(std/(len(tup)-1))


std_tup(tup)


# In[ ]:


import numpy as np

np.std(list(dict(tup).values()))


# <a style='text-decoration:none;line-height:16px;display:flex;color:#5B5B62;padding:10px;justify-content:end;' href='https://deepnote.com?utm_source=created-in-deepnote-cell&projectId=27f61235-518c-418f-b2d9-2a8bbda63abd' target="_blank">
# <img alt='Created in deepnote.com' style='display:inline;max-height:16px;margin:0px;margin-right:7.5px;' src='data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iODBweCIgaGVpZ2h0PSI4MHB4IiB2aWV3Qm94PSIwIDAgODAgODAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDU0LjEgKDc2NDkwKSAtIGh0dHBzOi8vc2tldGNoYXBwLmNvbSAtLT4KICAgIDx0aXRsZT5Hcm91cCAzPC90aXRsZT4KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPgogICAgPGcgaWQ9IkxhbmRpbmciIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJBcnRib2FyZCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEyMzUuMDAwMDAwLCAtNzkuMDAwMDAwKSI+CiAgICAgICAgICAgIDxnIGlkPSJHcm91cC0zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjM1LjAwMDAwMCwgNzkuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBpZD0iUGF0aC0yMCIgZmlsbD0iIzAyNjVCNCIgcG9pbnRzPSIyLjM3NjIzNzYyIDgwIDM4LjA0NzY2NjcgODAgNTcuODIxNzgyMiA3My44MDU3NTkyIDU3LjgyMTc4MjIgMzIuNzU5MjczOSAzOS4xNDAyMjc4IDMxLjY4MzE2ODMiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0zNS4wMDc3MTgsODAgQzQyLjkwNjIwMDcsNzYuNDU0OTM1OCA0Ny41NjQ5MTY3LDcxLjU0MjI2NzEgNDguOTgzODY2LDY1LjI2MTk5MzkgQzUxLjExMjI4OTksNTUuODQxNTg0MiA0MS42NzcxNzk1LDQ5LjIxMjIyODQgMjUuNjIzOTg0Niw0OS4yMTIyMjg0IEMyNS40ODQ5Mjg5LDQ5LjEyNjg0NDggMjkuODI2MTI5Niw0My4yODM4MjQ4IDM4LjY0NzU4NjksMzEuNjgzMTY4MyBMNzIuODcxMjg3MSwzMi41NTQ0MjUgTDY1LjI4MDk3Myw2Ny42NzYzNDIxIEw1MS4xMTIyODk5LDc3LjM3NjE0NCBMMzUuMDA3NzE4LDgwIFoiIGlkPSJQYXRoLTIyIiBmaWxsPSIjMDAyODY4Ij48L3BhdGg+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNMCwzNy43MzA0NDA1IEwyNy4xMTQ1MzcsMC4yNTcxMTE0MzYgQzYyLjM3MTUxMjMsLTEuOTkwNzE3MDEgODAsMTAuNTAwMzkyNyA4MCwzNy43MzA0NDA1IEM4MCw2NC45NjA0ODgyIDY0Ljc3NjUwMzgsNzkuMDUwMzQxNCAzNC4zMjk1MTEzLDgwIEM0Ny4wNTUzNDg5LDc3LjU2NzA4MDggNTMuNDE4MjY3Nyw3MC4zMTM2MTAzIDUzLjQxODI2NzcsNTguMjM5NTg4NSBDNTMuNDE4MjY3Nyw0MC4xMjg1NTU3IDM2LjMwMzk1NDQsMzcuNzMwNDQwNSAyNS4yMjc0MTcsMzcuNzMwNDQwNSBDMTcuODQzMDU4NiwzNy43MzA0NDA1IDkuNDMzOTE5NjYsMzcuNzMwNDQwNSAwLDM3LjczMDQ0MDUgWiIgaWQ9IlBhdGgtMTkiIGZpbGw9IiMzNzkzRUYiPjwvcGF0aD4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+' > </img>
# Created in <span style='font-weight:600;margin-left:4px;'>Deepnote</span></a>
