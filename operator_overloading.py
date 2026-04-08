class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # ─── Without Operator Overloading ───────────────────────────
    # Must be called explicitly as a method: v1.add(v2)
    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # ─── With Operator Overloading ───────────────────────────────
    # Called automatically when + is used: v1 + v2
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 4)
v2 = Vector(1, 3)

# ─── Without Operator Overloading ────────────────────────────────
result1 = v1.add(v2)
print("Without Operator Overloading:", result1)  # Output: Vector(3, 7)

# ─── With Operator Overloading ───────────────────────────────────
result2 = v1 + v2
print("With Operator Overloading:   ", result2)  # Output: Vector(3, 7)