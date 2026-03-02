class ViewModelBase:
    """
    Базовый класс ViewModel - View подписываются на свойства VM
    """

    def __init__(self):
        self._bindings = {}

    def bind(self, prop, callback):
        self._bindings.setdefault(prop, []).append(callback)

    def notify_vm(self, prop):
        for cb in self._bindings.get(prop, []):
            cb()
