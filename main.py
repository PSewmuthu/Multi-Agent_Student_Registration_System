"""
20APP4488
P.S.A.Singhe
https://github.com/PSewmuthu/Multi-Agent_Student_Registration_System.git
"""


class StudentRegistrationAgent:
    def __init__(self):
        '''
        Student Registration Agent: Please enter your name and student ID. 
        Student: John Doe, 12345 
        Student Registration Agent: Welcome, John Doe (ID: 12345). Proceeding to course selection.
        '''

        inpts = []

        while True:
            inpts = [itm.strip() for itm in input(
                "\nStudent Registration Agent: Please enter your name and student ID.\nStudent: ").split(',')]

            if len(inpts) == 2:
                break
            else:
                print(
                    "\nStudent Registration Agent: Please enter your name and student ID correctly. (Name, ID)")

        self.registration(inpts[0], inpts[1])

    def registration(self, name, id):
        print(
            f"\nStudent Registration Agent: Welcome, {name} (ID: {id}). Proceeding to course selection.\n\n")


class CourseSelectionAgent:
    def __init__(self):
        self.courses = {
            'Data Structures': 300,
            'Algorithms': 350,
            'Machine Learning': 400
        }

        self.show_menu()

    def show_menu(self):
        '''
        Course Selection Agent: Available courses are: 
        1. Data Structures - $300 
        2. Algorithms - $350 
        3. Machine Learning - $400 
        Please type the courses you want to register for (separate by commas).
        '''

        print("Course Selection Agent: Available courses are:")

        for ind, (name, price) in enumerate(self.courses.items()):
            print(f"{ind}. {name}\t - \t${price}")

        print("Please type the courses you want to register for (separate by commas).")
