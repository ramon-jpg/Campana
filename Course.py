class Course:
    def __init__(self, course_id, name, year, section):
        self.course_id = course_id
        self.name = name
        self.year = year
        self.section = section
        self.enrolled_students = []

    def enroll_student(self, student_name):
        if student_name not in self.enrolled_students:
            self.enrolled_students.append(student_name)
            print(f"{student_name} has been enrolled in {self.name}.")
        else:
            print(f"{student_name} is already enrolled in {self.name}.")

    def display_students(self):
        if self.enrolled_students:
            print(f"Students enrolled in {self.name}: {', '.join(self.enrolled_students)}")
        else:
            print(f"No students are enrolled in {self.name}.")

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}, Year: {self.year}, Section: {self.section}"


class CourseEnrollmentSystem:
    def __init__(self):
        self.courses = []

    def add_course(self, course_id, name, year, section):
        new_course = Course(course_id, name, year, section)
        self.courses.append(new_course)
        print(f"Course {name} has been added.")

    def enroll_student_in_course(self, course_id, student_name):
        for course in self.courses:
            if course.course_id == course_id:
                course.enroll_student(student_name)
                return
        print(f"Course with ID {course_id} not found.")

    def display_all_courses(self):
        if self.courses:
            print("Courses available:")
            for course in self.courses:
                print(course)
        else:
            print("No courses available.")

    def display_students_in_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                course.display_students()
                return
        print(f"Course with ID {course_id} not found.")


def main():
    system = CourseEnrollmentSystem()

    while True:
        print("\nCourse Enrollment System")
        print("1. Add Course")
        print("2. Enroll Student in Course")
        print("3. Display All Courses")
        print("4. Display Students in a Course")
        print("5. Exit")

        choice = input("Select an action (1-5): ")

        if choice == '1':
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            year = int(input("Enter year level: "))
            section = input("Enter section: ")
            system.add_course(course_id, name, year, section)

        elif choice == '2':
            course_id = input("Enter course ID to enroll in: ")
            student_name = input("Enter student name: ")
            system.enroll_student_in_course(course_id, student_name)

        elif choice == '3':
            system.display_all_courses()

        elif choice == '4':
            course_id = input("Enter course ID to display enrolled students: ")
            system.display_students_in_course(course_id)

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()