# Student Course Feedback System

# List to store all course feedback
course_feedback = []

def add_feedback():
    """
    This function collects course name and feedback
    from the user and stores it in the course_feedback list.
    """
    course = input("Enter course name: ").strip()
    comment = input("Enter feedback: ").strip()

    feedback = {
        "course": course,
        "comment": comment
    }

    course_feedback.append(feedback)
    print("Feedback submitted successfully.\n")

def view_feedback():
    """
    This function displays all submitted feedback.
    """
    if len(course_feedback) == 0:
        print("No feedback available.\n")
    else:
        print("\n--- Course Feedback ---")
        for index, fb in enumerate(course_feedback, start=1):
            print(f"{index}. Course: {fb['course']} | Feedback: {fb['comment']}")
        print()

def main():
    """
    Main function that controls program execution
    using a menu-driven approach.
    """
    while True:
        print("Student Course Feedback System")
        print("1. Add Feedback")
        print("2. View Feedback")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_feedback()
        elif choice == "2":
            view_feedback()
        elif choice == "3":
            print("Exiting program. Thank you.")
            break
        else:
            print("Invalid option. Please try again.\n")

# Program execution starts here
main()