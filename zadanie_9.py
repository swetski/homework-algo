#!/usr/bin/env python
# coding: utf-8

# In[3]:


from collections.abc import MutableSequence
import logging

# Настройка простого логирования
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


# Класс обёртка над списком 
# ведёт как список, но считает сколько вызывались методы добавления элементов

class CountingList(MutableSequence):

    def __init__(self, initial=None):
        # Внутри храню настоящий список
        self._data = list(initial or [])
        # Счётчик вызовов методов добавления
        self.add_calls = 0

# Сами методы добавления элементов

        # Добавление в конец списка
    def append(self, value):
        self.add_calls += 1        
        self._data.append(value)
        
        # Вставка элемента по индексу
    def insert(self, index, value):
        self.add_calls += 1
        self._data.insert(index, value)

        # Добавление нескольких элементов
    def extend(self, values):
        self.add_calls += 1
        self._data.extend(values)
        
        # Операция list += [1,2]       
    def __iadd__(self, values):
        self.add_calls += 1
        self._data += list(values)
        return self


# Методы для MutableSequence

        # Возвращает длину списка
    def __len__(self):
        return len(self._data)
    
       # Позволяет писать list[i]
    def __getitem__(self, i):
        return self._data[i]

      # Позволяет менять элемент list[i] = x
    def __setitem__(self, i, value):
        self._data[i] = value

      # Позволяет удалять элементы del list[i]
    def __delitem__(self, i):
        del self._data[i]

      # Вывод списка
    def __repr__(self):
        return repr(self._data)


# Метод test (ничего не знает)
def test(lst):
    log.info("Метод test вызван. Длина списка: %s", len(lst))


# Основной запуск
if __name__ == "__main__":

    # Создаю спец список
    lst = CountingList()

    # Передаю туда 5 чисел
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(4)
    lst.append(5)

    # Вызываю test
    test(lst)

    # После завершения test вывожу количество вызовов add
    log.info("Количество вызовов добавления: %s", lst.add_calls)


# In[ ]:




