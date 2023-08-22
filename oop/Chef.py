class Employee:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill


class Chef(Employee):
    def __init__(self, name, skill):
        super().__init__(name, skill)