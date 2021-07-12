from typing import Any


class ValidateFields:

    def length(self, var_value: Any, max: int, min: int = None):
        if var_value > max:
            raise ValueError("asldknaldknasld;")