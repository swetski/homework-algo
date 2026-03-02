class Observable:
    """
    Базовый класс для модели - позволяет подписываться на изменения
    """

    def __init__(self):
        self._listeners = []

    def subscribe(self, listener):
        self._listeners.append(listener)

    def notify(self, field_name):
        for listener in list(self._listeners):
            listener(field_name)
