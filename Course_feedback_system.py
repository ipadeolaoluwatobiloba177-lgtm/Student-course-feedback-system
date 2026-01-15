course_feedback = []

def add_feedback():
    course = input("Enter course name: ")
    comment = input("Enter feedback: ")
    course_feedback.append({"course": course, "comment": comment})
    print("Feedback submitted successfully")

def view_feedback():
    if not course_feedback:
        print("No feedback available")
    else:
        for fb in course_feedback:
            print("Course:", fb["course"], "| Feedback:", fb["comment"])

def main():
    while True:
        print("1. Add Feedback")
        print("2. View Feedback")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_feedback()
        elif choice == "2":
            view_feedback()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
