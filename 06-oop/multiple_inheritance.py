class Teacher:
    def __init__(self,subject):
        self.subject=subject

    def teach(self):
        return f"Teaching: {self.subject}"

class Student:
    def __init__(self,courses):
        self.courses=courses
    def study(self):
        return f"Studying: {self.courses}"

class TeachingAssistant(Teacher,Student):
    def __init__(self,subject,courses):
        self.subject=subject
        self.courses=courses

TA=TeachingAssistant("Biology","Microbiology")
print(TA.teach())
print(TA.study())    
    