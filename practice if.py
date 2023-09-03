#!usr/bin/env python3

#Tyler Kirkwood
age = (int(input("input age here: ")))
if age > 17:
    print("You can see a rated R movie")
elif age < 17 and age > 12:
    print("You can see a rated PG-13 movie")
else:
    print("You can only see rated PG movies")