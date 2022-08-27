#!/usr/bin/env python
# coding: utf-8

# # Problem 1: Calculating weighted-average for all the elements in a given list.

# In[ ]:


def norm_weights(weights):

    weights_sum = 0
    for i in range(len(weights)):
        if type(weights[i]) != int and type(weights[i]) != float:
            return('!!! Please input correct datatype')
        weights_sum = weights_sum + weights[i]
    return [i/weights_sum for i in weights]

def weighted_avg(lst, weights):
    weights = norm_weights(weights)
    assert len(weights) == len(lst)
    weighted_sum = 0
    for i in range(len(lst)):
        if type(lst[i]) != int and type(lst[i]) != float:
            return('!!! Please input correct datatype')
        weighted_sum = weighted_sum + lst[i]*weights[i]
    return weighted_sum/len(lst)

def unweighted_avg(lst):
    # weights = norm_weights(weights)
    # assert len(weights) == len(lst)
    unweighted_sum = 0
    for i in range(len(lst)):
        if type(lst[i]) != int and type(lst[i]) != float:
            return('!!! Please input correct datatype')
        unweighted_sum = unweighted_sum + lst[i]
    return unweighted_sum/len(lst)


# In[ ]:


lst_1 = [3.86, -16, 167, 32, -99, complex('83+24j')]
lst_2 = [3.86, -16, 167, 32, -99, '83']
lst_3 = [3.86, -16, 167, 32, -99, 83]
weights = [1, 2, 3, 4, 5, 6]

weighted_avg(lst_3, weights), unweighted_avg(lst_3)
# norm_weights(weights)


# In[ ]:


a = input()


# In[ ]:


a[0]


# In[ ]:


lst_input = input('Enter elements of a list separated by comma: ')
weights_input = input('Enter elements of a weights separated by comma: ')
print("\n")
lst = lst_input.split(',')
weights = weights_input.split(',')

for i in range(len(lst)):
    # convert each item to int type
    lst[i] = float(lst[i])
    weights[i] = float(weights[i])


# In[ ]:


weighted_avg(lst, weights), unweighted_avg(lst)


# # Problem 2(a): Palindrome

# In[ ]:


def check_rev(string):
    if type(string)!=str:
        return('!! Enter a valid input')
    return string == string[::-1]   ## string[::-1]


# In[ ]:


check_rev('nan')


# # Problem 2(b): Reversing words in a string

# In[ ]:


def rev_string_1(string):
    ## Verifying the input type
    if type(string)!=str:
        return('!! Provide a valid input')
    ## spliting string by spaces and storing them into a list 's' in reverse order [::-1] ([start:stop:step]) is same as [-1::-1].
    s = string.split()[::-1]
    ## joining all the elements of the list with space in between to get the reversed string
    return(" ".join(s))


# In[ ]:


rev_string_1("we have tutorial for our course every friday")


# In[ ]:


def rev_string_2(string):
    if type(string)!=str:
        return('!! Provide a valid input')
    s = string.split()
    l = []
    for i in s:
        ## reversing every element of 's' and storing to a new list 'l'.
        l.append(i[::-1])
    return(" ".join(l))


# In[ ]:


def rev_string_3(string):
    if type(string)!=str:
        return('!! Provide a valid input')
    s = string.split()[::-1]
    l = []
    for i in s:
        ## reversing every element of 's' and storing to a new list 'l'.
        l.append(i[::-1])
    return(" ".join(l))


# In[ ]:


## "we have tutorial for our course every friday"

string = input('Input the desired string: ')
rev_string_1(string), rev_string_2(string)


# # Problem 3: 

# In[ ]:


def remove_empty_seq(lst):
    if type(lst) != list:
        return("!! Provide a valid input")
    for i in lst[:]:
        if (type(i) == list) or (type(i) == str) or (type(i) == tuple):
            if len(i) == 0:
                lst.remove(i)
    return lst


# In[ ]:


remove_empty_seq(['', 4, 7.4, 'drt84', complex('4+5j'), (), '', 'gfq7', []])


# In[ ]:


len(())


# <a style='text-decoration:none;line-height:16px;display:flex;color:#5B5B62;padding:10px;justify-content:end;' href='https://deepnote.com?utm_source=created-in-deepnote-cell&projectId=50c685f8-20da-4e07-a47b-804ae8bddebe' target="_blank">
# <img alt='Created in deepnote.com' style='display:inline;max-height:16px;margin:0px;margin-right:7.5px;' src='data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iODBweCIgaGVpZ2h0PSI4MHB4IiB2aWV3Qm94PSIwIDAgODAgODAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDU0LjEgKDc2NDkwKSAtIGh0dHBzOi8vc2tldGNoYXBwLmNvbSAtLT4KICAgIDx0aXRsZT5Hcm91cCAzPC90aXRsZT4KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPgogICAgPGcgaWQ9IkxhbmRpbmciIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJBcnRib2FyZCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEyMzUuMDAwMDAwLCAtNzkuMDAwMDAwKSI+CiAgICAgICAgICAgIDxnIGlkPSJHcm91cC0zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjM1LjAwMDAwMCwgNzkuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBpZD0iUGF0aC0yMCIgZmlsbD0iIzAyNjVCNCIgcG9pbnRzPSIyLjM3NjIzNzYyIDgwIDM4LjA0NzY2NjcgODAgNTcuODIxNzgyMiA3My44MDU3NTkyIDU3LjgyMTc4MjIgMzIuNzU5MjczOSAzOS4xNDAyMjc4IDMxLjY4MzE2ODMiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0zNS4wMDc3MTgsODAgQzQyLjkwNjIwMDcsNzYuNDU0OTM1OCA0Ny41NjQ5MTY3LDcxLjU0MjI2NzEgNDguOTgzODY2LDY1LjI2MTk5MzkgQzUxLjExMjI4OTksNTUuODQxNTg0MiA0MS42NzcxNzk1LDQ5LjIxMjIyODQgMjUuNjIzOTg0Niw0OS4yMTIyMjg0IEMyNS40ODQ5Mjg5LDQ5LjEyNjg0NDggMjkuODI2MTI5Niw0My4yODM4MjQ4IDM4LjY0NzU4NjksMzEuNjgzMTY4MyBMNzIuODcxMjg3MSwzMi41NTQ0MjUgTDY1LjI4MDk3Myw2Ny42NzYzNDIxIEw1MS4xMTIyODk5LDc3LjM3NjE0NCBMMzUuMDA3NzE4LDgwIFoiIGlkPSJQYXRoLTIyIiBmaWxsPSIjMDAyODY4Ij48L3BhdGg+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNMCwzNy43MzA0NDA1IEwyNy4xMTQ1MzcsMC4yNTcxMTE0MzYgQzYyLjM3MTUxMjMsLTEuOTkwNzE3MDEgODAsMTAuNTAwMzkyNyA4MCwzNy43MzA0NDA1IEM4MCw2NC45NjA0ODgyIDY0Ljc3NjUwMzgsNzkuMDUwMzQxNCAzNC4zMjk1MTEzLDgwIEM0Ny4wNTUzNDg5LDc3LjU2NzA4MDggNTMuNDE4MjY3Nyw3MC4zMTM2MTAzIDUzLjQxODI2NzcsNTguMjM5NTg4NSBDNTMuNDE4MjY3Nyw0MC4xMjg1NTU3IDM2LjMwMzk1NDQsMzcuNzMwNDQwNSAyNS4yMjc0MTcsMzcuNzMwNDQwNSBDMTcuODQzMDU4NiwzNy43MzA0NDA1IDkuNDMzOTE5NjYsMzcuNzMwNDQwNSAwLDM3LjczMDQ0MDUgWiIgaWQ9IlBhdGgtMTkiIGZpbGw9IiMzNzkzRUYiPjwvcGF0aD4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+' > </img>
# Created in <span style='font-weight:600;margin-left:4px;'>Deepnote</span></a>
