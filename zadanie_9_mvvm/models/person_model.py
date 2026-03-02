from core.observable import Observable


class PersonModel(Observable):
    """Модель хранит данные и операции
    """

    def __init__(self, name=""):
        super().__init__()
        self._name = name

    @property
    def name(self):
        return self._name

    def set_name(self, value):
        if value == self._name:
            return
        self._name = value
        self.notify("name")

    def clear(self):
        self.set_name("")
