# ============================================================
# CLASS VARIABLE vs INSTANCE VARIABLE
# Example: Employee
# ============================================================

class Employee:

    # ── Class Variables ──────────────────────────────────────
    # Defined INSIDE class but OUTSIDE __init__
    # Shared across ALL instances (employees)
    # Access by: Employee.variable OR self.variable
    company_name     = "TechCorp Inc."
    total_employees  = 0

    def __init__(self, name, salary):

        # ── Instance Variables ───────────────────────────────
        # Defined INSIDE __init__ using 'self'
        # Unique to EACH instance (employee)
        # Access by: self.variable ONLY

        Employee.total_employees += 1          # class variable updated by ALL objects
        self.employee_id = Employee.total_employees   # unique per employee
        self.name        = name                       # unique per employee
        self.salary      = salary                     # unique per employee

    def display_info(self):
        print(f"  ID      : {self.employee_id}")      # instance variable
        print(f"  Name    : {self.name}")              # instance variable
        print(f"  Salary  : ${self.salary:,}")         # instance variable
        print(f"  Company : {Employee.company_name}")  # class variable (same for all)


# ── Creating Employees ───────────────────────────────────────
emp1 = Employee("Alice", 90000)
emp2 = Employee("Bob",   70000)
emp3 = Employee("Carol", 65000)

# ── Display Info ─────────────────────────────────────────────
print("\n👤 Employee 1:")
emp1.display_info()

print("\n👤 Employee 2:")
emp2.display_info()

print("\n👤 Employee 3:")
emp3.display_info()


# ============================================================
# DIFFERENCE 1: Class variable is SAME for all objects
# ============================================================
print("\n✅ Class Variable — same for ALL employees:")
print(f"  emp1.company_name : {emp1.company_name}")   # TechCorp Inc.
print(f"  emp2.company_name : {emp2.company_name}")   # TechCorp Inc.
print(f"  emp3.company_name : {emp3.company_name}")   # TechCorp Inc.


# ============================================================
# DIFFERENCE 2: Instance variable is UNIQUE per object
# ============================================================
print("\n✅ Instance Variable — unique for EACH employee:")
print(f"  emp1.name : {emp1.name}")    # Alice
print(f"  emp2.name : {emp2.name}")    # Bob
print(f"  emp3.name : {emp3.name}")    # Carol


# ============================================================
# DIFFERENCE 3: Changing class variable affects ALL objects
# ============================================================
print("\n🔄 Changing class variable (company_name)...")
Employee.company_name = "InnovateTech Ltd."   # changed once at class level

print("  After change:")
print(f"  emp1.company_name : {emp1.company_name}")   # InnovateTech Ltd.
print(f"  emp2.company_name : {emp2.company_name}")   # InnovateTech Ltd.
print(f"  emp3.company_name : {emp3.company_name}")   # InnovateTech Ltd.


# ============================================================
# DIFFERENCE 4: Changing instance variable affects ONLY that object
# ============================================================
print("\n🔄 Changing instance variable (salary of Alice only)...")
emp1.salary += 10000   # only emp1 is affected

print("  After change:")
print(f"  emp1.salary : ${emp1.salary:,}")   # $100,000  ← changed
print(f"  emp2.salary : ${emp2.salary:,}")   # $ 70,000  ← unchanged
print(f"  emp3.salary : ${emp3.salary:,}")   # $ 65,000  ← unchanged


# ============================================================
# DIFFERENCE 5: Class variable tracks shared state (total count)
# ============================================================
print(f"\n📊 Total Employees (class variable) : {Employee.total_employees}")  # 3