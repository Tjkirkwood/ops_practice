#!/usr/bin/env python3
from random import randint

class Monster:
    species = 'elf'
    hp = 10
    atk = 3
    is_dead = False

    def __init__(self, species, hp, atk):
        self.species = species
        self.hp = hp
        self.atk = atk
        self.defense = randint(0, 2)
    
    def attack(self):
        strike = randint
        print(f'{self.species} hits for {strike} damage points')
        return strike
    
    def take_damage(self, dmg):
        dmg -= self.defense
        print(f'{self.species} is hit for {dmg} points!')
        self.hp -= dmg
        if self.hp <= 0:
            print(f'{self.species}has died!')
            self.is_dead = True