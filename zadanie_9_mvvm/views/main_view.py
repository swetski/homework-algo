import tkinter as tk
from views.widgets import BoundEntry, BoundButton


def create_view(root, vm):
    tk.Label(root, text="Мини MVVM Demo", font=("Arial", 14)).pack(pady=8)

    BoundEntry(root, vm, "name", "Поле 1:")
    BoundEntry(root, vm, "name", "Поле 2:")
    BoundEntry(root, vm, "name", "Поле 3:")

    BoundButton(root, "Очистить", vm.clear_command)
