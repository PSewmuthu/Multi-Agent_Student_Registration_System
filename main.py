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

        self.name = inpts[0]
        self.id = inpts[1]

        self.registration()

    def registration(self):
        print(
            f"\nStudent Registration Agent: Welcome, {self.name} (ID: {self.id}). Proceeding to course selection.\n\n")

    def finalize(self):
        '''
        Student Registration Agent: Your registration is complete. Thank you for registering, John Doe!
        '''

        print(
            f"\n\nStudent Registration Agent: Your registration is complete. Thank you for registering, {self.name}!\n")


class CourseSelectionAgent:
    def __init__(self):
        self.courses = {
            'Data Structures': 300,
            'Algorithms': 350,
            'Machine Learning': 400
        }

        self.show_menu()
        self.confirm()

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

    def confirm(self):
        '''
        Student: Data Structures, Machine Learning
        Course Selection Agent: You have selected Data Structures and Machine Learning. The total cost is $700.
        '''

        selected = []

        while True:
            selected = [subject.strip().lower() for subject in input("")]

            if selected == []:
                print("Course Selection Agent: Please select at least one course.")
            else:
                break

        availables = []
        total = 0

        for subject in self.courses:
            if subject.lower() in selected:
                availables.append(subject)
                total += self.courses[subject]

        courses = ''

        if availables == []:
            print("Course Selection Agent: All you entered courses are not available.")
        elif len(availables) == 1:
            courses = availables[0]
        else:
            courses = ', '.join(availables[:-1]) + ', and ' + availables[-1]

        print(
            f"Course Selection Agent: You have selected {courses}. The total cost is ${total}.")


class PaymentAgent:
    def __init__(self):
        '''
        Payment Agent: Please enter your payment amount.
        Student: 700
        '''

        print("\n\nPayment Agent: Please enter your payment amount.\n")
        val = 0

        while True:
            try:
                val = int(input("Student: "))
                   if val > 0:
                        break
                    else:
                        print("\nPayment Agent: Please enter a valid amount.\n")
            except:
                print("\nPayment Agent: Please enter a valid amount.\n")
        
        self.pay(val)
    
    def pay(self,amount):
        '''
        Payment Agent: Payment of $700 received. Your registration is confirmed.
        '''
        
        print(f"\nPayment Agent: Payment of ${amount} received. Your registration is confirmed.")
