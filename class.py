#!/usr/bin/env python3
# author name: Tyler Kirkwood

class Person:
  def __init__(self, name, age, food):
    self.name = name
    self.age = age
    self.food = food

p1 = Person("Tyler", 26, "pizza")
p2 = Person("same", 33,"burger")

print(p1.name)
print(p1.age)
print(p1.food)
print(f'Hi {p1.name} your {p1.age} and your favourite food is {p1.food}')

print(p2.food)