#!/usr/bin/env python
# coding: utf-8

# In[5]:


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()


# Вставĸа: добавление слова в дерево.

# In[6]:


# вставляю слово
def insert(self, word):
    node = self.root

    for ch in word:
        if ch not in node.children:
            node.children[ch] = TrieNode()
        node = node.children[ch]

    node.is_end = True


# Поисĸ: поисĸ всего слова в дереве.

# In[7]:


# ищу полное слово
def search(self, word):
    node = self.root

    for ch in word:
        if ch not in node.children:
            return False
        node = node.children[ch]

    return node.is_end


# Поисĸ по префиĸсу: возвращает все слова, ĸоторые начинаются с префиĸса.

# In[15]:


# ищу по префиксу
def starts_with(self, prefix):
    node = self.root

    for ch in prefix:
        if ch not in node.children:
            return []
        node = node.children[ch]

    results = []
    stack = [(node, "")]

    while stack:
        curr, suffix = stack.pop()

        if curr.is_end:
            results.append(prefix + suffix)

        for c, nxt in curr.children.items():
            stack.append((nxt, suffix + c))

    return results

