"""
Aqsa Shahid
Lab 11, class in Python (extra points)
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = {}  # Store grades in a dictionary
    
    def add_grade(self, subject, grade):
        self.grades[subject] = float(grade)
    
    def get_average_grade(self):
        if not self.grades:  # Check if there are any grades
            return 0
        return sum(self.grades.values()) / len(self.grades)

# Create students
student1 = Student("Anna", 20)
student2 = Student("Robert", 25)

# Add grades
student1.add_grade("English", 78.5)
student1.add_grade("Math", 80.5)
student1.add_grade("Science", 92.0)

student2.add_grade("Math", 90.0)
student2.add_grade("Science", 88.5)
student2.add_grade("History", 95.0)
student2.add_grade("English", 82.0)

# Print student1 information
print(f"Student: {student1.name}, Age: {student1.age}")
print(f"Grades: {student1.grades}")
print(f"Average Grade: {student1.get_average_grade():.2f}")
print()

# Print student2 information
print(f"Student: {student2.name}, Age: {student2.age}")
print(f"Grades: {student2.grades}")
print(f"Average Grade: {student2.get_average_grade():.2f}")