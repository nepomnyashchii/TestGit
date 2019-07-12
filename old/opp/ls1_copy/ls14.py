class Person:
    species = "Human"

print (Person.species)
Person.alive = True
print(Person.alive)

man = Person ()
print(man.species)
print(man.alive)
Person.alive = False
print(man.alive)

man.name = "Darth"
man.surname = "Vader"
print(man.name, man.surname)
