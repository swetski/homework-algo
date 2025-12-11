#!/usr/bin/env python
# coding: utf-8

# Решение задания по схеме сети маршрутизаторов/серверов, обменивающихся сетевым трафиком.

# Условие:
# если между двумя узлами сети есть связь, они соединены
# ребром. Для каждого ребра указана номинальная пропускная способность среды и процент потерянных пакетов во время передачи.

# Задание: выразить данную схему в двух формах: с использованием
# массива и с использованием узлов.

# ВАРИАНТ 1. РЕШЕНИЕ ЧЕРЕЗ УЗЛЫ (Node + Edge)

# In[1]:


class Edge:
    def __init__(self, to, capacity, loss_percent):
        self.to = to
        self.capacity = capacity
        self.loss_percent = loss_percent


class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def add_edge(self, to, capacity, loss_percent):
        edge = Edge(to, capacity, loss_percent)
        self.edges.append(edge)


def connect(a, b, capacity, loss_percent):
    a.add_edge(b, capacity, loss_percent)
    b.add_edge(a, capacity, loss_percent)


# узлы (маршрутизаторы/серверы)
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")

# рёбра по схеме (не беру обозначение %, выведу потом)
connect(A, B, 1500, 90)
connect(A, C, 2000, 10)
connect(A, D, 1000, 50)
connect(B, F, 1500, 60)
connect(C, F, 500, 20)
connect(C, E, 900, 5)
connect(D, E, 2500, 1)
connect(E, F, 300, 85)


# печатаю граф
def print_graph(nodes):
    for node in nodes:
        neighbors_info = []
        for edge in node.edges:
            neighbors_info.append(
                f"{edge.to.name}(cap={edge.capacity}, loss={edge.loss_percent}%)"
            )
        print(f"{node.name} -- " + ", ".join(neighbors_info))


print_graph([A, B, C, D, E, F])


# ВАРИАНТ 2. РЕШЕНИЕ ЧЕРЕЗ МАССИВЫ (матрицы смежности)

# In[3]:


# узлы по индексам
NAMES = ["A", "B", "C", "D", "E", "F"]
N = len(NAMES)

# Матрица пропускных способностей (0 = нет ребра)
capacity = [[0] * N for _ in range(N)]
# Матрица потерь в процентах (0 = нет ребра)
loss_percent = [[0] * N for _ in range(N)]


def index(name):
    # Нахожу индекс вершины по имени
    return NAMES.index(name)


def add_edge(name1, name2, cap, loss):
     # Добавляю ребро в граф (туда-обратно)
    i = index(name1)
    j = index(name2)
    capacity[i][j] = cap
    capacity[j][i] = cap
    loss_percent[i][j] = loss
    loss_percent[j][i] = loss


# рёбра по схеме
add_edge("A", "B", 1500, 90)
add_edge("A", "C", 2000, 10)
add_edge("A", "D", 1000, 50)
add_edge("B", "F", 1500, 60)
add_edge("C", "F", 500, 20)
add_edge("C", "E", 900, 5)
add_edge("D", "E", 2500, 1)
add_edge("E", "F", 300, 85)


def print_matrix(matrix, title):
    print(title)
    # узлы
    print("    " + " ".join(f"{name:>6}" for name in NAMES))
    # матрица
    for i, row in enumerate(matrix):
        row_str = " ".join(f"{value:>6}" for value in row)
        print(f"{NAMES[i]:>2}  {row_str}")
    print()

print_matrix(capacity, "Матрица пропускных способностей")
print_matrix(loss_percent, "Матрица потерь (в %)")


# In[ ]:




