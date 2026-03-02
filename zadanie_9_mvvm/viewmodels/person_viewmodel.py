from core.viewmodel_base import ViewModelBase


class PersonViewModel(ViewModelBase):
    """ViewModel управляет моделью и уведомляет View
    """

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.model.subscribe(self._on_model_changed)

    def _on_model_changed(self, field_name):
        if field_name == "name":
            self.notify_vm("name")

    @property
    def name(self):
        return self.model.name

    @name.setter
    def name(self, value):
        self.model.set_name(value)

    def clear_command(self):
        self.model.clear()
