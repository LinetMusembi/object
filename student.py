
class Student:
    school = "AkiraChix"
    def __init__(self,first_name,last_name,age,nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
    def greet_student(self):
        return f"Hello {self.name},welcome to {self.school},are you a {self.nationality} by birth?"
    
    def show_full_name(self):
        full_name = self.first_name,+" ",+self.last_name
        return full_name
    
    def year_of_birth(self):
        return f"{2023 -self.age}"

    def show_initial(self):
        return self.first_name[0],self.last_name[0]


