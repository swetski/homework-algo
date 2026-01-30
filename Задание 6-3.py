#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque
from typing import List, Tuple


# Функция

# In[2]:


def lcs(a, b):
    # размеры строк
    n = len(a)
    m = len(b)

    # таблица (n+1) x (m+1) заполненная нулями
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # заполняю dp
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # восстановление подпоследовательности (иду назад)
    i = n
    j = m
    result = []

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            result.append(a[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    result.reverse()
    return "".join(result)


# Тест

# In[3]:


assert lcs("abcde", "ace") == "ace"
assert lcs("abc", "abc") == "abc"
assert lcs("abc", "def") == ""
assert lcs("", "abc") == ""
assert lcs("ABCBDAB", "BDCABA") in {"BCBA", "BDAB", "BCAB"}

print("Тесты прошли")

