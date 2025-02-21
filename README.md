# 📌 Multi-Agent Student Registration System

## 📖 Overview

This project was developed as part of the **Computer Laboratory** module. It implements a **multi-agent system** using Python to handle university student registration efficiently.

## 🎯 Purpose

The goal of this project is to automate and streamline the student registration process by using multiple agents, each responsible for a specific task:

1. **📝 Student Registration Agent** – Manages student details such as name and student ID.
2. **📚 Course Selection Agent** – Allows students to choose courses, verifies prerequisites, and calculates the total cost.
3. **💳 Payment Agent** – Handles payments, verifies sufficient funds, and confirms successful registration.

This system provides an interactive command-line interface where students can register for courses, make payments, and receive confirmation of their enrollment.

## ✨ Features

- ✅ User-friendly command-line interface
- ✅ Automated course selection and cost calculation
- ✅ Secure payment processing
- ✅ Step-by-step registration confirmation

## ⚙️ Installation & Usage

### 📌 Prerequisites

- Python 3.x installed

### 🛠️ Installation Steps

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/multi-agent-registration.git
   ```
2. Navigate to the project directory:
   ```sh
   cd multi-agent-registration
   ```
3. Run the script:
   ```sh
   python main.py
   ```

## 🚀 Example Usage

```
Student: Enter your name: John Doe
Student: Enter your student ID: 12345
Student Registration Agent: Welcome, John Doe (ID: 12345). Proceeding to course selection.

Course Selection Agent: Available courses are:
1. Data Structures - $300
2. Algorithms - $350
3. Machine Learning - $400
Student: Data Structures, Machine Learning
Course Selection Agent: You have selected Data Structures and Machine Learning. The total cost is $700.

Payment Agent: Please enter your payment amount.
Student: 700
Payment Agent: Payment of $700 received. Your registration is confirmed.
Student Registration Agent: Your registration is complete. Thank you for registering, John Doe!
```

## 🤝 Contributions

Contributions are welcome! Feel free to fork the repository and submit pull requests.
