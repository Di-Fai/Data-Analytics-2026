# Student Roster Manager
# Concepts: class, objects, encapsulation, getters, setters
# Author: Dimitri Nji

class Student:
    # Class attribute - shared by all students
    school = "YearUp Academy"

    def __init__(self, name, grade, track):
        # Instance attributes
        self.name = name
        self.__grade = grade
        self.track = track

    # Getter method - safely reads the private grade
    def get_grade(self):
        return self.__grade

    # Setter method - updates grade only if it is valid
    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
        else:
            print("Invalid grade! Must be 0-100.")

    # Display method - prints student report
    def display_info(self):
        print(f"""
===== YearUp Academy — Student Report =====
School : {Student.school}
Name   : {self.name}
Grade  : {self.get_grade()}
Track  : {self.track}
===========================================
""")


# Create two student objects
student1 = Student("Alice", 95, "Software Development")
student2 = Student("Brian", 88, "Data Analytics")

# Getter: read the private grade
print(student1.get_grade())
print(student2.get_grade())

# Setter: valid and invalid updates
student1.set_grade(98)
student1.set_grade(150)

# Display student reports
student1.display_info()
student2.display_info()