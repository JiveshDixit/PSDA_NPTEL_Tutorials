#!/usr/bin/env python
# coding: utf-8

# # Problem 1: Multiplication of two matrices

# In[ ]:


def matrix_multiplication(mat1, mat2):
    assert len(mat1[0]) == len(mat2), "Matrices are incompatible for multiplication!"
    return [[sum(a * b for a, b in zip(mat1_row, mat2_col)) for mat2_col in zip(*mat2)] for mat1_row in mat1]


# In[ ]:


mat1 = [[1, 3, 5], [3, 7, 11], [2, 5, 7]]
mat2 = [[11, 13, 17, 19], [3, 9, 27, 81], [2, 4, 16, 256]]

# mat1 = exec(mat1)
# mat2 = exec(mat2)

print(matrix_multiplication(mat1, mat2))
et = time.time()
print(et-st)


# In[ ]:


mat1 = [[1, 3, 5], 
        [3, 7, 11], 
        [2, 5, 7]]
mat2 = [[11, 13, 17, 19], 
        [3, 9, 27, 81], 
        [2, 4, 16, 256]]

assert len(mat1[0]) == len(mat2), "Matrices are incompatible for multiplication!"
result = [[0 for b_col in range(len(mat2[0]))] for a_row in range(len(mat1))]
 
# iterating by row of mat1
for i in range(len(mat1)):
 
    # iterating by column by mat2
    for j in range(len(mat2[0])):
 
        # iterating by rows of mat2
        for k in range(len(mat2)):
            result[i][j] += mat1[i][k] * mat2[k][j]
 
result


# In[ ]:





# # Problem 2: Sen’s slope

# In[ ]:


def in_sort(lst):
    for indx in range (len(lst)):
        i = indx
        while i > 0 and lst[i] < lst[i-1]:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i -= 1


# In[ ]:


def sen_slope(lst):

    slope_lst = []
    for i in range (len(lst)):
        for j in range (i+1, len(lst)):   ## since j>i
            slope_lst.append((lst[j] - lst[i])/(j-i))
    in_sort(slope_lst)
    if len(slope_lst)%2 !=0:
        return slope_lst[int((len(slope_lst)+1)/2)]
    else:
        return (slope_lst[int(len(slope_lst)/2)] + slope_lst[int(len(slope_lst)/2 + 1)])/2
    

## 12, 34, 22, 13, 89, -12, 32, -9


# In[ ]:


lst_input = input('Enter numbers for the list separated by comma: ')
lst = lst_input.split(',')

for i, j in enumerate(lst):   ### for i, j in zip(range(len(lst)), lst)
    j = float(j)
    lst[i] = j

sen_slope(lst)


# # Problem 3: Ratio of multiplication of column elements to the multiplication of diagonal elements for all the columns

# In[ ]:


def col_diag_ratio(matrx):
    assert len(matrx) == len(matrx[0]), "Input is not a square matrix"
    dia_mult = 1
    for i in range (len(matrx)):
        dia_mult = dia_mult*matrx[i][i]
    if dia_mult == 0:
        return "ratio is not defined"

    req_ratio = []
    for i in range (len(matrx)):
        col_multply = 1
        for j in range (len(matrx)):
            col_multply = col_multply*matrx[j][i]
        req_ratio.append(col_multply/dia_mult)
    return req_ratio


# In[ ]:


matrx = [[2, 4, 6, 45], [3, 5, 7, 29], [11, 13, 15, 91], [5, 18, 27, 97]]
col_diag_ratio(matrx)


# <a style='text-decoration:none;line-height:16px;display:flex;color:#5B5B62;padding:10px;justify-content:end;' href='https://deepnote.com?utm_source=created-in-deepnote-cell&projectId=eba7a261-284e-41e0-a7c9-fdd2d0e57690' target="_blank">
# <img alt='Created in deepnote.com' style='display:inline;max-height:16px;margin:0px;margin-right:7.5px;' src='data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iODBweCIgaGVpZ2h0PSI4MHB4IiB2aWV3Qm94PSIwIDAgODAgODAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDU0LjEgKDc2NDkwKSAtIGh0dHBzOi8vc2tldGNoYXBwLmNvbSAtLT4KICAgIDx0aXRsZT5Hcm91cCAzPC90aXRsZT4KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPgogICAgPGcgaWQ9IkxhbmRpbmciIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJBcnRib2FyZCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEyMzUuMDAwMDAwLCAtNzkuMDAwMDAwKSI+CiAgICAgICAgICAgIDxnIGlkPSJHcm91cC0zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjM1LjAwMDAwMCwgNzkuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBpZD0iUGF0aC0yMCIgZmlsbD0iIzAyNjVCNCIgcG9pbnRzPSIyLjM3NjIzNzYyIDgwIDM4LjA0NzY2NjcgODAgNTcuODIxNzgyMiA3My44MDU3NTkyIDU3LjgyMTc4MjIgMzIuNzU5MjczOSAzOS4xNDAyMjc4IDMxLjY4MzE2ODMiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0zNS4wMDc3MTgsODAgQzQyLjkwNjIwMDcsNzYuNDU0OTM1OCA0Ny41NjQ5MTY3LDcxLjU0MjI2NzEgNDguOTgzODY2LDY1LjI2MTk5MzkgQzUxLjExMjI4OTksNTUuODQxNTg0MiA0MS42NzcxNzk1LDQ5LjIxMjIyODQgMjUuNjIzOTg0Niw0OS4yMTIyMjg0IEMyNS40ODQ5Mjg5LDQ5LjEyNjg0NDggMjkuODI2MTI5Niw0My4yODM4MjQ4IDM4LjY0NzU4NjksMzEuNjgzMTY4MyBMNzIuODcxMjg3MSwzMi41NTQ0MjUgTDY1LjI4MDk3Myw2Ny42NzYzNDIxIEw1MS4xMTIyODk5LDc3LjM3NjE0NCBMMzUuMDA3NzE4LDgwIFoiIGlkPSJQYXRoLTIyIiBmaWxsPSIjMDAyODY4Ij48L3BhdGg+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNMCwzNy43MzA0NDA1IEwyNy4xMTQ1MzcsMC4yNTcxMTE0MzYgQzYyLjM3MTUxMjMsLTEuOTkwNzE3MDEgODAsMTAuNTAwMzkyNyA4MCwzNy43MzA0NDA1IEM4MCw2NC45NjA0ODgyIDY0Ljc3NjUwMzgsNzkuMDUwMzQxNCAzNC4zMjk1MTEzLDgwIEM0Ny4wNTUzNDg5LDc3LjU2NzA4MDggNTMuNDE4MjY3Nyw3MC4zMTM2MTAzIDUzLjQxODI2NzcsNTguMjM5NTg4NSBDNTMuNDE4MjY3Nyw0MC4xMjg1NTU3IDM2LjMwMzk1NDQsMzcuNzMwNDQwNSAyNS4yMjc0MTcsMzcuNzMwNDQwNSBDMTcuODQzMDU4NiwzNy43MzA0NDA1IDkuNDMzOTE5NjYsMzcuNzMwNDQwNSAwLDM3LjczMDQ0MDUgWiIgaWQ9IlBhdGgtMTkiIGZpbGw9IiMzNzkzRUYiPjwvcGF0aD4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+' > </img>
# Created in <span style='font-weight:600;margin-left:4px;'>Deepnote</span></a>
