from PySide2.QtWidgets import QLabel, QWidget, QLineEdit

from src.components.Field import Field, FunctionField, NumberField


class FieldFactory:
    def __init__(self):
        self.created_fields = {}

    def create_field(self, name: str, label: QLabel, w: QWidget) -> QWidget:
        field = Field(label, w)
        self.created_fields[name] = field
        return field

    def create_function_field(self, name: str, label: QLabel, line_edit: QLineEdit) -> FunctionField:
        field = FunctionField(label, line_edit)
        self.created_fields[name] = field
        return field

    def create_number_field(self, name: str, label: QLabel, line_edit: QLineEdit) -> NumberField:
        field = NumberField(label, line_edit)
        self.created_fields[name] = field
        return field

    def get_created_fields(self):
        return self.created_fields
