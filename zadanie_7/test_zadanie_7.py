#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pytest

from zadanie_7 import Trie


def test_insert_and_search_basic():
    t = Trie()
    t.insert("cat")
    t.insert("car")

    assert t.search("cat") is True
    assert t.search("car") is True
    assert t.search("ca") is False      # префикс есть, но слово не добавляли
    assert t.search("cap") is False     # такого пути нет


def test_starts_with_basic():
    t = Trie()
    for w in ["cat", "car", "caar", "dog"]:
        t.insert(w)

    res = t.starts_with("ca")
    assert set(res) == {"cat", "car", "caar"}  # порядок не важен


def test_starts_with_not_found():
    t = Trie()
    t.insert("cat")
    assert t.starts_with("zz") == []


def test_empty_trie():
    t = Trie()
    assert t.search("a") is False
    assert t.starts_with("a") == []


def test_word_is_prefix_of_another():
    t = Trie()
    t.insert("a")
    t.insert("ab")

    assert t.search("a") is True
    assert t.search("ab") is True
    assert set(t.starts_with("a")) == {"a", "ab"}

