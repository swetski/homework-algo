import tkinter as tk
from models.person_model import PersonModel
from viewmodels.person_viewmodel import PersonViewModel
from views.main_view import create_view


def main():
    root = tk.Tk()
    root.title("Mini MVVM Framework")

    model = PersonModel("Вася")
    vm = PersonViewModel(model)

    create_view(root, vm)

    root.mainloop()


if __name__ == "__main__":
    main()
