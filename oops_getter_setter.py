class MyClass:
    def __init__(self, value):
        # Initialize the private attribute _value with the provided argument
        self._value = value

    def show(self):
        # Print the current internal _value (not the ten_value)
        print(f"value is {self._value}")

    @property
    def ten_value(self):
        # Getter: returns 10 times the internal _value
        # Accessed like an attribute: obj.ten_value
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, new_value):
        # Setter: when you assign to obj.ten_value,
        # it reverse-calculates and updates _value as new_value / 40
        # Example: obj.ten_value = 120 → _value = 120 / 40 = 3.0
        self._value = new_value / 40


obj = MyClass(20)         # _value = 20
obj.ten_value = 120       # Setter called → _value = 120 / 40 = 3.0
                          # Try commenting this line: _value stays 20, ten_value = 200
obj.show()                # Prints: value is 3.0
print(obj.ten_value)      # Getter called → prints: 30.0  (3.0 * 10)