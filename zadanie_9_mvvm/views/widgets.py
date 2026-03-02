import tkinter as tk


class BoundEntry:
    """
    Обёртка над Entry - Двусторонний биндинг с ViewModel
    """

    def __init__(self, parent, vm, prop, label):
        self.vm = vm
        self.prop = prop
        self._updating = False

        frame = tk.Frame(parent)
        frame.pack(fill="x", pady=4)

        tk.Label(frame, text=label, width=18, anchor="w").pack(side="left")

        self.var = tk.StringVar(value=getattr(vm, prop))
        entry = tk.Entry(frame, textvariable=self.var)
        entry.pack(side="left", fill="x", expand=True)

        self.var.trace_add("write", self._on_text_changed)
        vm.bind(prop, self._on_vm_changed)

    def _on_text_changed(self, *_):
        if self._updating:
            return
        setattr(self.vm, self.prop, self.var.get())

    def _on_vm_changed(self):
        self._updating = True
        try:
            self.var.set(getattr(self.vm, self.prop))
        finally:
            self._updating = False


class BoundButton:
    """
    Обёртка над Button
    """

    def __init__(self, parent, text, command):
        button = tk.Button(parent, text=text, command=command)
        button.pack(pady=6)
