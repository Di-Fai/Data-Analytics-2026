student = ("Alice", 20, "Data Analytics", 3.5, True)

print(student)
print(f"Name   : {student[0]}")
print(f"Age    : {student[1]}")
print(f"Major  : {student[2]}")
print(f"GPA    : {student[3]}")
print(f"Active : {student[4]}")
print(f"Length : {len(student)}")

# count(x)

t = (1, 2, 2,  3, 2)
print(t.count(2))

# index(x)

print(t.index(2))

# len(t)
print(len(t))

# min(t)
print(min(t))

# max(t)
print(max(t))

# sum(t)
print(sum(t))

#sorted(t)
print(sorted(t))

#type(t)
print(type(t))  


# --------------------------------------------------------------

# index
t = ("a", "b", "c")

print(t[0])
print(t[-1])


# slice
t = (1, 2, 3, 4, 5)

t[1:4]
print(t[1:4])

# concatenation
t = (1, 2, 3)
t2 = ("a", "b", "c")
t3 = t + t2
print(t3)


# repetition
t = (1, 2, 3)
print(t * 3)
print(t2)


#membership
t = (1, 2, 3)
print(2 in t)


#uniqueness
t = (1, 2, 2, 3, 4, 5)
print(len(set(t)))



