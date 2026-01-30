#!/usr/bin/env python
# coding: utf-8

# In[10]:


from collections import deque
from typing import List, Tuple


# Функция

# In[11]:


def topological_sort_adj_matrix(matrix):

    n = len(matrix)

    # Считаю входящие рёбра (зависимости) для каждой вершины
    indeg = [0] * n
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                indeg[j] += 1

    # Кладу в очередь вершины без зависимостей
    queue = deque()
    for i in range(n):
        if indeg[i] == 0:
            queue.append(i)

    # Здесь будет правильный порядок
    order = []

    # Пока есть вершины без зависимостей
    while queue:
        v = queue.popleft()
        order.append(v)

        # Убираю вершину v из графа
        for to in range(n):
            if matrix[v][to] != 0:
                indeg[to] -= 1
                if indeg[to] == 0:
                    queue.append(to)

    # Если не все вершины попали в порядок — есть цикл
    if len(order) != n:
        raise ValueError("В графе - цикл, топологическая сортировка невозможна")

    return order


# Тест

# In[12]:


# граф: 0 -> 1 -> 2
matrix = [
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 0]
]

result = topological_sort_adj_matrix(matrix)

assert result == [0, 1, 2]

print("Тест прошёл")


# In[ ]:




