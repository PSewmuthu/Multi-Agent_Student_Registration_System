"""
20APP4488
P.S.A.Singhe
https://github.com/PSewmuthu/Multi-Agent_Student_Registration_System.git
"""


class StudentRegistrationAgent:
    def __init__(self):
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
