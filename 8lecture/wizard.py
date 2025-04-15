"""OOP example - inheritance"""

class Wizard:
    """Super class"""
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    ...

class Student(Wizard):          # inherit from Wizard
    """Sub class"""
    def __init__(self, name, house):
        super().__init__(name)  # init Super class
        self.house = house
    ...

class Professor(Wizard):        # inherit from Wizard
    """Sub class"""
    def __init__(self, name, subject):
        super().__init__(name)  # init Super class
        self.subject = subject
    ...

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
profesor = Professor("Severus", "Defense Against the Dark Arts")
