#!/usr/bin/env python3 

class Dog:
    animal = 'dog'
 
    
    def __init__(self, breed, coat_color):
 
        self.breed = breed
        self.coat_color = coat_color
 

Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")
Buck = Dog("pitbull", "black with white spots")
 
print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Coat Color: ', Rodger.coat_color)


print('buzo details: ')
print('buzo is a', Buzo.breed)

print('Bill details: ')
print(f'Buck is a {Buck.breed}')
print(f'Buck is a {Buck.breed} and is {Buck.coat_color}')

