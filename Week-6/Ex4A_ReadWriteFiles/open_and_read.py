# Description: This script reads from about_me.txt
# Author: Dimitri Nji


f = open("about_me.txt", "a")

f.write("\nPerfect night out: For my perfect night out, I would go to a nice restaurant, enjoy good food, listen to music, and spend time with people I care about.\n")

f.close()

print("============================================")

f = open("about_me.txt", "r")

print(f.read())

f.close()

print("===========================================")

# Testing .read(50)
f = open("about_me.txt", "r")

print(f.read(50))
print(f.read(50))

f.close()

print("===========================================")

# Testing .readline()
f = open("about_me.txt", "r")

print(f.readline(10))
print(f.readline())

for i in range(1, 5):
    print(f.readline())

f.close()

print("==========================================")

# Testing .readlines()
f = open("about_me.txt", "r")

print(f.readlines(1))
print(f.readlines(1))
print(f.readlines(10))
print(f.readlines(10))
print(f.readlines(100))
print(f.readlines(-1))

f.close()

print("=========================================")

# Description: This script practices different file read methods
# Author: Dimitri Nji

f = open("about_me.txt", "r")

first_50 = f.read(50)

next_four_lines = []

for i in range(4):
    next_four_lines.append(f.readline())

next_100 = f.readlines(100)

print(f"First 50 characters: {first_50}")
print(f"Next four lines, as list by line: {next_four_lines}")
print(f"Next 100 characters, as list by line, rounded up to complete lines: {next_100}")

f.close()

'''This lab shows how to create, write, and read a text file using Python. 
The open() function opens the file. 
The "a" mode appends new information to the file, and the "r" mode reads from the file. The .read() method reads characters, .readline() reads one line at a time, and .
readlines() reads lines into a list.'''