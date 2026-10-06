students = ["Kai Samba", "Foday", "Sharon"]
print(students)
print()

# Accessing items in list by theri index
print(f"Student: {students[0]}")
print(f"Student: {students[1]}")
print(f"Student: {students[2]}")
print()

# Get the index of an item in a list
print(f"Index: {students.index(f"Kai Samba")}")
print(f"Index: {students.index(f"Sharon")}")
print(f"Index: {students.index(f"Foday")}")
print()

# Know the number of items in a string
print(f"Number of students: {len(students)}")
print()

# Add items to a list
students.append("Isatu")
print(students)
students += ["Kadiatu", "John", "Bintu"]
print()

# Add at a specific location
students.insert(0, "Gleekan")
print()

# Extending a list
fruits = ["Apple", "Banana", "Mango"]
students.extend(fruits)
print()

# Removing an item from a list
fruits.remove("Mango")
print()

students.pop()
students.pop()
students.pop()
print(students)
print()

last_item = students.pop()
print(f"Last Item: {last_item}")
print()

for student in students:
    print(f"Student: {student}")
print()

