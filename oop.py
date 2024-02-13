# object-oriented programing

#class Person:
   # def __init__(self):
    #    self.name = "Esther"
     #   self.age = 29
       # self.school = "emobilis"
      #  self.location = "Nairobi"


#person = Person()
##person.name = "Lucrecia"
 #person.location = "Nakuru"

#print(person.name)
#print(person.school)
#print(person.age)
#print(person.location)

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = People(name="Gianna", age=16)

person2 = People(name="Peter", age=19)

person3 = People(name="Leonne", age=18)


print(person1.name)
print(f"My name is {person1.name} and i am {person1.age} years old.")
print(f"My brother's name is {person2.name} and is {person2.age} years old.")
print(f"My cousin's name is {person3.name} which he shares with my dad and he is {person3.age} years old.")