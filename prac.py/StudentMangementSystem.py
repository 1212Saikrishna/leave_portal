# Functionalities:
# store student details
# rollno
# name
# address
# phonenumber
# class

############
# Here in this Project we develop to get some information regarding School.info
# get any student details
# update any student details
# remove any student details
# no.of students in school
# get all student details
# get particular student class student

# Functionalities:
# store student details
# rollno
# name
# address
# phonenumber
# class

############
# Here in this Project we develop to get some information regarding School.info
# get any student details
# update any student details
# remove any student details
# no.of students in school
# get all student details
# get particular student class student
# 1. Student Class:
# This class is designed to store and manage student details. It has the following attributes and methods:
# student_dictionary: A dictionary that stores student details.
# school_name: A class variable storing the default school name.
# __init__(): Constructor method to initialize student details by taking user input.
# It also adds the student to the student_dictionary and assigns the student to a particular class.
# getStudent(): Method to display the student's details.
# updateStudent(): Method to update student details, including the name, phone number, address, or class.
# updateSchoolName(): A class method to update the school name.
# getTotalStudentCount(): A class method to get the total number of students.

# 2. StudentClass Class:
# This class is designed to store and manage student classes. It has the following attributes and methods:
# classes: A dictionary that stores different student classes.
# __init__(): Constructor method to initialize a student class.

# 3. main() Function:
# This function is the main entry point of the program and provides a user interface to interact with the student and class data.
# It includes options to:
# Get student details.
# Add a new student.
# Remove a student.
# Update student details.
# Update the school name.
# Get the number of students in the school.
# Get details of all students.
# Get details of students in a particular class.

# 4. Program Execution:
# The program execution starts with the if __name__ == '__main__': block.
# It initializes a loop to allow users to perform multiple actions.
# Users can input their choice (1-8) to perform specific actions.
# The program handles these actions accordingly, such as adding, updating, or displaying student details, and updating the school name.
# Each part of the code and its functionalities are clearly explained in the comments within the code.
# This program acts as a basic student management system that allows you to interact with student and class data.

# Define a Student class to store student details.
class Student:
    student_dictionary = {}  # Dictionary to store student details.
    school_name = 'GODOLKIN UNIVERSITY'  # Default school name.

    # Constructor to initialize student details.
    def __init__(self):
        # Input student details from the user.
        self.roll_no = input('\n\tEnter the Student Roll Number: ')
        self.name = input('\tEnter the Student Name: ')
        self.phone_number = input('\tEnter the Student Phone Number: ')
        self.address = input('\tEnter the Student Address: ')
        student_class = input('\tEnter the Student Class[Ex: 1,2,3,4,5,6,7,8,9,10]: ')

        # Check if the class already exists, if not, create a new class.
        if student_class in StudentClass.classes:
            StudentClass.classes[student_class].studentList.append(self)
        else:
            new_class = StudentClass(student_class)
            new_class.studentList.append(self)
            StudentClass.classes[student_class] = new_class

        self.student_class = StudentClass.classes[student_class]

        print('\nStudent Added Successfully')
        self.getStudent()  # Display student details.

    # Method to display student details.
    def getStudent(self):
        print('\n---Student Details---\n')
        print('\tRoll Number:', self.roll_no)
        print('\tName:', self.name)
        print('\tPhone Number:', self.phone_number)
        print('\tAddress:', self.address)
        print('\tClass:', self.student_class.name)
        print(f'\tSchool Name: {Student.school_name}')

    # Method to update student details.
    def updateStudent(self):
        print('\t\tSelect Option to update student details\n')
        print('\t\t\t1) To Change Student Name')
        print('\t\t\t2) To Change Student Phone Number')
        print('\t\t\t3) To Change Student Address')
        print('\t\t\t4) To Change Student Class')
        option = input('\t\tEnter any above given option: ')
        option = int(option)
        print()

        if option in [1, 2, 3, 4]:
            if option == 1:
                self.name = input('\t\t\tEnter the Student New Name: ')
                print('\n\t\tStudent Name Changed Successfully\n')
            elif option == 2:
                self.phone_number = input('\t\t\tEnter the New Phone Number: ')
                print('\n\t\tStudent Phone Number Changed Successfully\n')
            elif option == 3:
                self.address = input('\t\t\tEnter the New Address: ')
                print('\n\t\tStudent Address Changed Successfully\n')
            elif option == 4:
                new_class = input('\n\t\tEnter the Student New Class Name: ')
                self.student_class.studentList.remove(self)
                try:
                    self.student_class = StudentClass.classes[new_class]
                    self.student_class.studentList.append(self)
                except:
                    addClass = StudentClass(new_class)
                    self.student_class = addClass
                    addClass.studentList.append(self)

            self.getStudent()
        else:
            print('\n\t\tYou have chosen the wrong option')

    # Class method to update the school name.
    @classmethod
    def updateSchoolName(cls, new_school_name):
        cls.school_name = new_school_name

    # Class method to get the total number of students.
    @classmethod
    def getTotalStudentCount(cls):
        return len(cls.student_dictionary)


# Define a StudentClass class to store student classes.
class StudentClass:
    classes = {}  # Dictionary to store student classes.

    # Constructor to initialize a student class.
    def __init__(self, name):
        self.name = name
        StudentClass.classes[name] = self
        self.studentList = []  # List to store students in the class.


# Define the main function to interact with the user.
def main():
    print(f'---WELCOME TO {Student.school_name}---\n')
    print('\t1) To Get Student Details')
    print('\t2) To Add New Student')
    print('\t3) To Remove Student')
    print('\t4) To Update Student Details')
    print('\t5) To Update School Name')
    print('\t6) To Get Number Of Students In School')
    print('\t7) To Get All Student Details')
    print('\t8) To Get Any Class Student Details')

    option = input('\nEnter Any Above Given option: ')
    option = int(option)
    print()

    if option == 1:
        roll_no = input('\tEnter the Roll Number of a Student: ')
        try:
            Student.student_dictionary[roll_no].getStudent()
        except:
            print('\t\tYou Have Entered the Wrong roll number')

    elif option == 2:
        new_student = Student()
        Student.student_dictionary[new_student.roll_no] = new_student

    elif option == 3:
        roll_no = input('\tEnter the Roll Number of a Student: ')
        try:
            student = Student.student_dictionary.pop(roll_no)
            student.student_class.studentList.remove(student)
            print(f'\t\t{roll_no} Student Deleted Successfully')
        except:
            print('\t\tNo Student there to delete')

    elif option == 4:
        roll_no = input('\tEnter the Roll Number of a Student: ')
        print()
        try:
            Student.student_dictionary[roll_no].updateStudent()
        except:
            print('\n\t\tYou Have Entered a Wrong Roll Number')

    elif option == 5:
        new_school_name = input('\tEnter the New School Name: ')
        Student.updateSchoolName(new_school_name)
        print(f'School Name Changed Successfully to {new_school_name}')

    elif option == 6:
        print('Total Number Of Students In School: ', Student.getTotalStudentCount())

    elif option == 7:
        if Student.student_dictionary:
            print('Total Number Of Students In School: ', Student.getTotalStudentCount())
            print('\nTotal Student List With Details\n')
            for sNo, student in enumerate(Student.student_dictionary.values()):
                print(f'Student - {sNo + 1}')
                student.getStudent()
                print()
        else:
            print('No Students There!')

    elif option == 8:
        try:
            class_name = input('\tEnter the Class Name: ')
            students = StudentClass.classes.get(class_name)
            if students:
                print(f'\nStudents Of Class - {students.name}')
                print(f'Total Number of Students In Class {students.name}: {len(students.studentList)}')
                print()
                for sNo, student in enumerate(students.studentList):
                    print(f'Student - {sNo + 1}')
                    student.getStudent()
                    print()
        except:
            print('\nYou Entered a Wrong Class Name or NO Students There!')


# Entry point of the program.
# if __name__ == '__main__':: This line checks whether the script is being run directly (as the main program) or 
# if it's being imported as a module into another script. 
# If the script is the main program,
# it will execute the code inside this block.

# option = 'y': This line initializes a variable option with the value 'y'. 
# It's used to control the loop that allows the user to continue running the program.
# while option == 'y':: This line starts a while loop. The loop will continue running as long as the value of the option variable is 'y'. 
# This means the loop will continue running as long as the user wants to continue.

# main(): This line calls the main() function.
# It's the entry point for the program, where the main functionality of the program is defined.
# option = input('\nDo you want to Continue [y/n]? : '): This line prompts the user for input. The input() function displays the message 
# "Do you want to Continue [y/n]? : " and waits for the user to type something. The user's input is then stored in the option variable.
# print(): This line adds a blank line for formatting purposes to separate the input prompt from the previous output or from the next iteration.
# The while loop continues to run until the user enters something other than 'y' when prompted. 
# If the user enters 'n' or anything else, the loop will exit, and the program will terminate.
# This code allows the user to run the main() function repeatedly by entering 'y' when asked if they want to continue. 
# It's a simple way to create a loop that keeps the program running until the user decides to exit.
if __name__ == '__main__':
    option = 'y'
    while option == 'y':
        main()
        option = input('\nDo you want to Continue [y/n]? : ')
        print()


