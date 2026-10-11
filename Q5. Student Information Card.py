#Take Input From User
S_name = input("Enter Student name: ")
Class_section = input("Enter Class with Section name: ")
School_name = input("Enter School name: ")

#FOrmating
print("-" * 5, "STUDENT ID CARD", "-" * 5)      
print(f"Name: {S_name}\nClass: {Class_section}\nSchool: {School_name}")
print("-" * 27)







#Alternative Code from AI
# A. Input
# 1. Ask the user for the student's name
student_name = input("Enter Student Name: ")

# 2. Ask for the class and section
class_section = input("Enter Class and Section (e.g., 8B): ")

# 3. Ask for the school name
school_name = input("Enter School Name: ")

# B. Formatting
# Print the structured student ID card using f-strings and neat layout
print("\n----- STUDENT ID CARD -----")
print(f"Name: {student_name}")
print(f"Class: {class_section}")
print(f"School: {school_name}")
print("----------------------------")
