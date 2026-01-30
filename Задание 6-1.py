#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque
from typing import List, Tuple


# Функция

# In[2]:


def adjacency_matrix_to_edges(matrix: List[List[int]]) -> List[Tuple[int, int, int]]:
    edges = []
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                edges.append((i, j, matrix[i][j]))

    return edges


# Тест

# In[3]:


def test_adj_matrix_to_edges_basic():
    m = [
        [0, 1, 0],
        [0, 0, 5],
        [2, 0, 0],
    ]
    assert adjacency_matrix_to_edges(m) == [(0, 1, 1), (1, 2, 5), (2, 0, 2)]

