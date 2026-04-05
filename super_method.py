class ParentClass:
    def parent_method(self):
        print("This is Parent Method in ParentClass")
        
class ChildClass(ParentClass):
    def parent_method(self):
        print("This is Parent Method in ChildClass")
        super().parent_method()
        
    def child_method(self):
        print("This is Child  Method in ChildClass")
        super().parent_method()
        
child_object = ChildClass()
child_object.child_method()
child_object.parent_method()
    