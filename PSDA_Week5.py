#!/usr/bin/env python
# coding: utf-8

# # Problem 1: Binary representations of two given numbers are anagram or not.

# In[ ]:


def DecToBin(num):
    lst_bin = []
    while (num>0):
        lst_bin.append(str(num%2))
        num=num//2
    lst_bin = lst_bin[::-1]
    return "".join(lst_bin)

    ## or bin(num) can be used to convert from decimal to binary

    # output of bin(num) = 0bxxx..., hence removing first two letters of 
    # output of bin(num) to get binary equivalent of given number

    ## https://www.cuemath.com/numbers/decimal-to-binary/  refer for definition for conversion
        


# In[ ]:


DecToBin(717), bin(717)[2:]


# In[ ]:


### This function is not relevant to problem 1.

## Conversion from binary to decimal

def BinToDec(binary):

    dec, i = 0, 0
    while(binary!=0):
        mod = binary % 10          ## 
        dec = dec + mod * pow(2, i)    ####  
        binary //= 10
        i = i+ 1
    return dec

    ## or int(binary, 2) shall also produce the resultant decimal integer from binary input.

    ## https://www.cuemath.com/numbers/binary-to-decimal/   refer for definition for conversion


# In[ ]:


BinToDec(1011001101), int(str(1011001101), 2)


# In[ ]:


## preparing a dictionary with keys '0' and '1' and 
## corrosponding values as their counting in the binary number. 

def counter_string(binary):
    lst_bin = list(binary)  ### or [i for i in "bin"]
    dict_bin = {}
    dict_bin['0'] = 0
    dict_bin['1'] = 0
    for i in lst_bin:
        if i == '0':
            dict_bin['0']+=1
        else:
            dict_bin['1']+=1
    return dict_bin


# In[ ]:


# Start writing code here...
def BinAnagramCheck(num1,num2):
  


    bin1 = DecToBin(num1)      ### bin(num1)[2:]
    bin2 = DecToBin(num2)      ### bin(num2)[2:]
  
    # append zeros at the left of the shorter length string
    # diff_len = (abs(len(bin1)-len(bin2)))
    if (len(bin1)>len(bin2)):
         bin2 = abs(len(bin1)-len(bin2)) * '0' + bin2    #### 3 * 's' = 'sss'
    else:
         bin1 = abs(len(bin1)-len(bin2)) * '0' + bin1
  
    # convert binary representations into dictionary
    dict1 = counter_string(bin1)
    dict2 = counter_string(bin2)
  
    # compare both dictionaries
    if dict1 == dict2:
         return True
    else:
         return False


# In[ ]:


DecToBin(3), DecToBin(7)


# In[ ]:


num1 = int(input('Input first integer: '))
num2 = int(input('Input second integer: '))

BinAnagramCheck(num1, num2)


# In[ ]:


# adding any number of zeros to the left of a binary number doesn't changes the number
100*'0' + bin(8)[2:] , bin(8)[2:] ,int(100*'0' + bin(8)[2:], 2)


# # Problem 2: Reading data from a file, and writing to a new file after doing some operations on the data

# In[ ]:


with open('input_test.txt', 'r') as f:   ### opening file
    lst = f.read().splitlines()          ### storing data into lst variable ['ele1', 'ele2', ...]

new_dict = {}
new_dict['Dec'] = []
new_dict['Bin'] = []
for i in lst:
    if i=='Decimal' or i=='Binary':
        pass
    else:
        if i.split('~')[0] == 'Dec':     #### ele.split(' ')   Dec:0  1275:1
            new_dict['Dec'].append(i.split('~')[1])
        elif i.split('~')[0] == 'Bin':
            new_dict['Bin'].append(i.split('~')[1])

inter_dict = {}
inter_dict['b2d'] = []
inter_dict['d2b'] = []
for i, j in new_dict.items():    ### {key:{key: value}}
    if i == 'Bin':
        for k in j:
            inter_dict['b2d'].append(int(k, 2))

    elif i == 'Dec':
        for k in j:
            inter_dict['d2b'].append(bin(int(k))[2:])


### writing data into a new file

with open('output_test.txt', 'w') as f:
    f.write('Binary')
    f.write('\n')
    for i in inter_dict['d2b']:
        f.write(str(i))
        f.write('\n')

    f.write('Decimal')
    f.write('\n')
    for j in inter_dict['b2d']:
        f.write(str(j))
        f.write('\n')
f.close()


# In[ ]:


### appending the data in an existing file
with open('output_test-3.txt', 'a') as f:
    f.write('\n')
    f.write('Binary')
    f.write('\n')
    for i in inter_dict['d2b']:
        f.write(str(i))
        f.write('\n')

    f.write('Decimal')
    f.write('\n')
    for j in inter_dict['b2d']:
        f.write(str(j))
        f.write('\n')
f.close()


# In[ ]:


### writing output next to input in a new file.

with open('output_test_1.txt', 'w') as f:
    f.write('Decimal \t \t \t Binary')
    f.write('\n')
    for i, j in zip(inter_dict['d2b'] , new_dict['Dec']):
        f.write(j + '\t \t \t' + str(i))
        f.write('\n')
    f.write('\n')
    f.write('Binary \t \t \t Decimal')
    f.write('\n')
    for i, j in zip(inter_dict['b2d'] , new_dict['Bin']):
        f.write(j + '\t \t \t' + str(i))
        f.write('\n')
f.close()


# # Problem 3: Removing associated keys and values for the given substring values

# In[ ]:


test_dict = {1 : 'Today is a Sunny day', 2 : 'Did you go to the school today?', 
                3 : 'Was the school open?', 4:'sunny days'}
 
# initializing substrings
sub_lst = ['sunny', 'school']
 
# Remove keys with substring values
# Using any() + generator expression
new_dict = dict()
for key, val in test_dict.items():
   if not any(i.capitalize() in val for i in sub_lst):
       new_dict[key] = val

# new_dict = {key : val for key, val in test_dict.items() if not any(ele in val for ele in sub_lst)}
new_dict


# <a style='text-decoration:none;line-height:16px;display:flex;color:#5B5B62;padding:10px;justify-content:end;' href='https://deepnote.com?utm_source=created-in-deepnote-cell&projectId=627d36a1-5de9-4824-abc9-c2bd72351003' target="_blank">
# <img alt='Created in deepnote.com' style='display:inline;max-height:16px;margin:0px;margin-right:7.5px;' src='data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iODBweCIgaGVpZ2h0PSI4MHB4IiB2aWV3Qm94PSIwIDAgODAgODAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDU0LjEgKDc2NDkwKSAtIGh0dHBzOi8vc2tldGNoYXBwLmNvbSAtLT4KICAgIDx0aXRsZT5Hcm91cCAzPC90aXRsZT4KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPgogICAgPGcgaWQ9IkxhbmRpbmciIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJBcnRib2FyZCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEyMzUuMDAwMDAwLCAtNzkuMDAwMDAwKSI+CiAgICAgICAgICAgIDxnIGlkPSJHcm91cC0zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjM1LjAwMDAwMCwgNzkuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBpZD0iUGF0aC0yMCIgZmlsbD0iIzAyNjVCNCIgcG9pbnRzPSIyLjM3NjIzNzYyIDgwIDM4LjA0NzY2NjcgODAgNTcuODIxNzgyMiA3My44MDU3NTkyIDU3LjgyMTc4MjIgMzIuNzU5MjczOSAzOS4xNDAyMjc4IDMxLjY4MzE2ODMiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0zNS4wMDc3MTgsODAgQzQyLjkwNjIwMDcsNzYuNDU0OTM1OCA0Ny41NjQ5MTY3LDcxLjU0MjI2NzEgNDguOTgzODY2LDY1LjI2MTk5MzkgQzUxLjExMjI4OTksNTUuODQxNTg0MiA0MS42NzcxNzk1LDQ5LjIxMjIyODQgMjUuNjIzOTg0Niw0OS4yMTIyMjg0IEMyNS40ODQ5Mjg5LDQ5LjEyNjg0NDggMjkuODI2MTI5Niw0My4yODM4MjQ4IDM4LjY0NzU4NjksMzEuNjgzMTY4MyBMNzIuODcxMjg3MSwzMi41NTQ0MjUgTDY1LjI4MDk3Myw2Ny42NzYzNDIxIEw1MS4xMTIyODk5LDc3LjM3NjE0NCBMMzUuMDA3NzE4LDgwIFoiIGlkPSJQYXRoLTIyIiBmaWxsPSIjMDAyODY4Ij48L3BhdGg+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNMCwzNy43MzA0NDA1IEwyNy4xMTQ1MzcsMC4yNTcxMTE0MzYgQzYyLjM3MTUxMjMsLTEuOTkwNzE3MDEgODAsMTAuNTAwMzkyNyA4MCwzNy43MzA0NDA1IEM4MCw2NC45NjA0ODgyIDY0Ljc3NjUwMzgsNzkuMDUwMzQxNCAzNC4zMjk1MTEzLDgwIEM0Ny4wNTUzNDg5LDc3LjU2NzA4MDggNTMuNDE4MjY3Nyw3MC4zMTM2MTAzIDUzLjQxODI2NzcsNTguMjM5NTg4NSBDNTMuNDE4MjY3Nyw0MC4xMjg1NTU3IDM2LjMwMzk1NDQsMzcuNzMwNDQwNSAyNS4yMjc0MTcsMzcuNzMwNDQwNSBDMTcuODQzMDU4NiwzNy43MzA0NDA1IDkuNDMzOTE5NjYsMzcuNzMwNDQwNSAwLDM3LjczMDQ0MDUgWiIgaWQ9IlBhdGgtMTkiIGZpbGw9IiMzNzkzRUYiPjwvcGF0aD4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+' > </img>
# Created in <span style='font-weight:600;margin-left:4px;'>Deepnote</span></a>
