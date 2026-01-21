Student Course Feedback System

Name: Ipadeola Oluwatobiloba Samuel
Matric No: 24/14733
Department: Computer Science

1. REQUIREMENT ANALYSIS
The Student Course Feedback System is designed to provide a simple platform where students can give feedback on courses they have taken. The system allows users to submit feedback for a specific course and also view all previously submitted feedback.
The main requirements of the system are:
The system should allow students to enter a course name.
The system should allow students to submit feedback comments.
The system should store multiple feedback entries during program execution.
The system should display all submitted feedback when requested.
The system should allow the user to exit the program safely.

2. SYSTEM DESIGN
Data Structure
The system uses a list named course_feedback to store feedback records. Each feedback record is stored as a dictionary containing:
The course name
The feedback comment
This structure makes it easy to store, access, and display feedback entries.

FUNCTIONAL DESIGN
The system is divided into the following functions:
add_feedback()
This function collects the course name and feedback comment from the user and stores them in the course_feedback list.
view_feedback()
This function displays all feedback that has been submitted. If no feedback exists, it notifies the user accordingly.
main()
This function controls the flow of the program by displaying a menu and responding to the user’s selection. It ensures the program runs continuously until the user chooses to exit.

3. IMPLEMENTATION
The system was implemented using the Python programming language. Core programming concepts such as lists, dictionaries, functions, loops, and conditional statements were used to achieve the desired functionality. The program runs in a command-line environment and interacts with the user through text input and output.

4. TESTING
The system was tested by:
Adding multiple course feedback entries.
Viewing feedback to ensure all entries were displayed correctly.
Entering invalid menu options to confirm proper error handling.
All system functions worked as expected during testing.

5. DEPLOYMENT
The completed program was uploaded to a GitHub repository to allow for version control, easy access, and future improvements. Deployment on GitHub also makes the system available for collaboration and review.

6. MAINTENANCE AND FUTURE ENHANCEMENTS
The system can be improved in future by:
Adding a rating system alongside feedback comments.
Storing feedback permanently using files or a database.
Allowing feedback editing and deletion.
Generating reports and analytics for course performance.
