#!/usr/bin/env python
# coding: utf-8

# In[2]:


from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict


def process_line(line):
    
    line = line.strip()

    if not line or ":" not in line:
        return None

    name, number = line.split(":", 1)

    name = name.strip()
    number = number.strip()

    if not number.isdigit():
        return None

    # форматирование имени
    name = name.lower().capitalize()

    return int(number), name


def group_people(filename):
    result = defaultdict(list)

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # параллельная обр-ка строк
    with ThreadPoolExecutor() as executor:
        processed = list(executor.map(process_line, lines))

    # убираю None потом группирую
    for item in processed:
        if item is not None:
            number, name = item
            result[number].append(name)

    return dict(result)


if __name__ == "__main__":
    data = group_people("people.txt")
    print(data)

