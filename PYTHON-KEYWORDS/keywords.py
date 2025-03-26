# Student Information System
# This program demonstrates the use of various Python keywords

# importing all the required modules
from datetime import datetime
import os
import json
import functools

# global variables for this system
global STUDENT_DATABASE
STUDENT_DATABASE = {}

# defining the main Student class
class Student:
    """Class to represent a student in our system"""
    
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = {}
        self.is_active = True  # using 'is' keyword in conditions later
    
    def enroll_course(self, course_name, credits):
        """Enroll student in a course"""
        # using 'if' and 'in' keywords
        if course_name in self.courses:
            # using 'raise' keyword
            raise ValueError(f"Student already enrolled in {course_name}")
        else:
            # using dictionary assignment
            self.courses[course_name] = {"credits": credits, "grade": None}
            return True
    
    def assign_grade(self, course_name, grade):
        """Assign grade to a course"""
        # using 'if', 'not', and 'in' keywords
        if not course_name in self.courses:
            # using 'return' keyword
            return False
        
        # using 'elif' and 'and' keywords
        elif grade < 0 or grade > 100:
            # using 'assert' keyword
            assert False, "Grade must be between 0 and 100"
        else:
            self.courses[course_name]["grade"] = grade
            return True
    
    def calculate_gpa(self):
        """Calculate the GPA based on courses and grades"""
        total_points = 0
        total_credits = 0
        
        # using 'for' keyword
        for course, details in self.courses.items():
            # using 'continue' keyword
            if details["grade"] is None:
                continue
            
            total_credits += details["credits"]
            total_points += details["grade"] * details["credits"]
        
        # using 'if' keyword with comparison
        if total_credits == 0:
            # using 'return' with 'None' keyword
            return None
        
        return total_points / total_credits
    
    def drop_course(self, course_name):
        """Drop a course"""
        # using 'if' and 'in' keywords
        if course_name in self.courses:
            # using 'del' keyword
            del self.courses[course_name]
            return True
        return False
    
    def get_transcript(self):
        """Get student transcript with all courses and grades"""
        transcript = {
            "student_id": self.student_id,
            "name": self.name,
            "courses": self.courses,
            "gpa": self.calculate_gpa()
        }
        return transcript
    
    # using 'nonlocal' keyword in a nested function
    def update_personal_info(self, **kwargs):
        """Update student personal information"""
        def update_fields():
            nonlocal kwargs
            
            # using 'for' keyword with dictionary items
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
        
        update_fields()
        return True


# Function to add a new student
def add_student(student_id, name, age):
    """Add a new student to the database"""
    # using 'if', 'in', and 'or' keywords
    if student_id in STUDENT_DATABASE or student_id <= 0:
        # using 'False' keyword
        return False
    
    # using class instantiation
    STUDENT_DATABASE[student_id] = Student(student_id, name, age)
    # using 'True' keyword
    return True


# Function to get student by ID
def get_student(student_id):
    """Get a student by ID"""
    # using 'try', 'except', and 'finally' keywords
    try:
        # using dictionary access
        return STUDENT_DATABASE[student_id]
    except KeyError:
        print(f"Student with ID {student_id} not found")
        return None
    finally:
        # using 'pass' keyword in a finally block
        pass


# Function to list all students
def list_all_students():
    """List all students in the database"""
    # using 'if' and 'not' keywords
    if not STUDENT_DATABASE:
        print("No students in the database")
        return []
    
    return list(STUDENT_DATABASE.values())


# Function to delete a student
def delete_student(student_id):
    """Delete a student from the database"""
    # using 'if', 'in', and 'not' keywords
    if not student_id in STUDENT_DATABASE:
        return False
    
    # using 'del' keyword
    del STUDENT_DATABASE[student_id]
    return True


# Function to save database to file
def save_database(filename="students.json"):
    """Save the student database to a JSON file"""
    # using 'with' keyword for file operations
    with open(filename, 'w') as f:
        # We can't directly serialize Student objects, so we'll convert them
        serializable_db = {}
        
        # using 'for' keyword
        for student_id, student in STUDENT_DATABASE.items():
            serializable_db[student_id] = {
                "student_id": student.student_id,
                "name": student.name,
                "age": student.age,
                "courses": student.courses,
                "is_active": student.is_active
            }
        
        json.dump(serializable_db, f, indent=4)
    
    return True


# Function to load database from file
def load_database(filename="students.json"):
    """Load the student database from a JSON file"""
    global STUDENT_DATABASE
    
    # using 'try', 'except', and 'else' keywords
    try:
        # using 'with' keyword
        with open(filename, 'r') as f:
            serialized_db = json.load(f)
    except FileNotFoundError:
        print(f"Database file {filename} not found")
        return False
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}")
        return False
    else:
        # Reconstruct our Student objects
        STUDENT_DATABASE = {}
        
        # using 'for' keyword
        for student_id, data in serialized_db.items():
            # Convert string keys back to integers
            student_id = int(student_id)
            student = Student(data["student_id"], data["name"], data["age"])
            student.courses = data["courses"]
            student.is_active = data["is_active"]
            STUDENT_DATABASE[student_id] = student
        
        return True


# Using 'lambda' keyword to create a simple filter function
get_active_students = lambda: [s for s in STUDENT_DATABASE.values() if s.is_active is True]


# Generator function using 'yield' keyword
def course_enrollment_report():
    """Generate a report of course enrollments"""
    course_counts = {}
    
    # using 'for' keyword
    for student in STUDENT_DATABASE.values():
        for course in student.courses:
            if course in course_counts:
                course_counts[course] += 1
            else:
                course_counts[course] = 1
    
    # using 'yield' keyword
    for course, count in sorted(course_counts.items(), key=lambda x: x[1], reverse=True):
        yield f"Course: {course}, Enrollment: {count}"


# Function to demonstrate 'break' keyword
def find_student_by_name(name):
    """Find a student by name"""
    # using 'for' and 'break' keywords
    for student_id, student in STUDENT_DATABASE.items():
        if student.name.lower() == name.lower():
            print(f"Found student: {student.name} (ID: {student.student_id})")
            break
    else:
        # This runs if the loop completes without a break
        print(f"No student found with name: {name}")


# Function to demonstrate 'as' keyword with context manager
def export_transcript(student_id, filename=None):
    """Export a student's transcript to a file"""
    student = get_student(student_id)
    
    if not student:
        return False
    
    if filename is None:
        filename = f"transcript_{student.name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.txt"
    
    # using 'with' and 'as' keywords
    with open(filename, 'w') as transcript_file:
        transcript = student.get_transcript()
        transcript_file.write(f"Transcript for {transcript['name']} (ID: {transcript['student_id']})\n")
        transcript_file.write(f"GPA: {transcript['gpa'] if transcript['gpa'] is not None else 'N/A'}\n\n")
        transcript_file.write("Courses:\n")
        
        for course, details in transcript['courses'].items():
            grade = details['grade'] if details['grade'] is not None else 'Not graded'
            transcript_file.write(f"- {course}: {grade} (Credits: {details['credits']})\n")
    
    return True


# Main function to run the program
def main():
    """Main function to demonstrate the Student Information System"""
    print("Welcome to the Student Information System!")
    
    # sample students
    add_student(1, "John Mark Cabuhat", 20)
    add_student(2, "Jeffrey Policarpio", 19)
    add_student(3, "Charles Banagan", 21)
    
    # Enroll students in courses
    student1 = get_student(1)
    student1.enroll_course("Python Programming", 3)
    student1.enroll_course("Data Structures", 4)
    student1.assign_grade("Multimedia", 95)
    
    student2 = get_student(2)
    student2.enroll_course("Python Programming", 3)
    student2.enroll_course("Web Development", 3)
    student2.assign_grade("Python Programming", 88)
    student2.assign_grade("Web Development", 92)
    
    student3 = get_student(3)
    student3.enroll_course("Database Systems", 4)
    student3.enroll_course("Data Structures", 4)
    student3.assign_grade("Database Systems", 78)
    student3.assign_grade("Data Structures", 85)
    
    # Print all students
    print("\nAll Students:")
    for student in list_all_students():
        print(f"- {student.name} (ID: {student.student_id})")
    
    # Print course enrollment report
    print("\nCourse Enrollment Report:")
    for report_line in course_enrollment_report():
        print(report_line)
    
    # Export a transcript
    export_transcript(2)
    print(f"\nExported transcript for John Mark")
    
    # Save the database
    save_database()
    print("\nSaved student database to students.json")
    
    print("\nThank you for using the Student Information System!")


# Using the 'if' keyword with '__name__' check
if __name__ == "__main__":
    main()
