#!env/bin/env python3

#author Tyler Kirkwood


numbers = [7,3,13,6,8,5,1,2,4,15,9,10,12,14,11]
lessFfnum = []
lessNums = []

for num in numbers:
    if num < 10:
        lessFfnum.append(num) 
        lessFfnum.sort()


print(lessFfnum)
print()  

num = int(input("Enter a number: ")) #Get a number from user
for n in numbers:
    if n < num: #Compare user number against numbers in list
        lessNums.append(n) #Add numbers that are less than user name to our list
        lessNums.sort() # Sort list
# Print the list
print(lessNums)