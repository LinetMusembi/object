# Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

    # def __str__(self):
    #     return f"{self.name}({self.age}) " 


    def my_func(self):
        print("Hello my name is"+" " +self.name)   

person = Person("Lynet",50)
person.age = 30
# person.my_func()
# person2 = Person("Fel",24)
# person3 = Person("Irene",30)
print(person.age)

# print(person.age)
# print(person2.name)
# print(person3.name)
# print(person3.age)

# Insert a function that prints a greeting, and execute it on the p1 object:

class Student:
    def __init__(self,name,sex,profession):
        self.name = name
        self.name = sex
        self.profession = profession

    def show(self):
        print("Name:",self.name,"Sex:",self.sex)


