#!/usr/bin/env python3

'''
generate a list of random numbers and letters
'''

import sys
import random as r
import os

names = ['alpha', 'beta', 'gamma', 'test', 'example', 'banana', 'orange', 'apple', 'capybara', 'kangaroo', 'network', 'program', 'quiz', 'output']

suffixes = ['txt', 'md', 'py', 'sh']

numbers = range(0, 9)

def randofilename(percentage=20):
    maxrange = (100 - percentage) + 1 
    if r.randint(0, maxrange) == 0:
        return r.choice(names) + str(r.choice(numbers))
    else:
        return r.choice(names) + str(r.choice(numbers)) + '.' + r.choice(suffixes)

def randotouch(randofile):
    x = os.system('touch ' + 'test/' + randofile)
    if x:
        print('An error occurred.')

def headsortails(percentage):
    "given a percentage chance of true, flip a coin"
    max = (100 - percentage) + 1
    fraction = (r.randint(0, max)) / 100
    return bool(fraction)

def randofile(file, filesize, outputfile='test/datafile.txt'):
    with open(outputfile, 'a') as f:
        f.write(file + ':' + str(filesize) + '\n')

def write_lines(filename, parent, numlines):
    with open(os.path.join(parent, filename), 'w') as f:
        for i in range(0, numlines):
            f.write(r.choice(names) + '\n')


def write_bytes(filename, numbytes):
    "fill up file with specified data"
    stringthing = "All work and no play makes Jack a dull boy."
    complete = len(stringthing) + 1  # add 1 for newline character
    count = numbytes
    f = open('test/' + filename, 'w')
    while count > complete:
        f.write(stringthing + '\n')
        count -= complete
    count2 = count
    while count2 > 0:
        x = count - count2
        if x == len(stringthing):
            x = 0
        f.write(stringthing[x])
        count2 -= 1
    f.close()



if __name__ == "__main__":
    try:
        total = sys.argv[1]
    except:
        total = 10
    try:
        parent = 'finaldir'
        os.mkdir(parent)
    except:
        print(f'ERROR: having trouble creating {parent}. Delete it and run again.')
        exit()
    for i in range(0, int(total)):
        dog = randofilename()
        size = r.randint(0, 20)
        write_lines(dog, parent, size)
