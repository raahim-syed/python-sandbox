class Person:
    def __init__(self, name, major, gpa, isOnProbation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.isOnProbation = isOnProbation
    def onHonorRole(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
    def willHeSucceedInLife(self, bool = False):
        if not bool:
            return self.name + " is a failure at life."
        else: 
            return self.name + " will succeed at life"
    


student = Person("Raahim", "BSCS", 2.6, False)
student2 = Person("Shahmeer", "BSCS", 2.8, False)
student3 = Person("Sallar", "BSCS", 3.85, False)

print(student.name)
print(student.onHonorRole())
print(student.willHeSucceedInLife())

print(student2.willHeSucceedInLife(True))

print(student3.willHeSucceedInLife(True))
print(student3.onHonorRole())