Problem Statement: Project Tracker

Educational institutions often face challenges in managing and tracking student assignments effectively. Majority Faculty members lack a centralized system to create, schedule, monitor, and grade assignments, while students need a streamlined interface to manage, prioritize, and submit their work on time. Current manual or scattered systems lead to inefficiencies, miscommunication, missed deadlines, and grading delays.
There is a need for a unified Project Tracker platform that enables:
•	Faculty to efficiently assign, manage, and evaluate assignments.
•	Students to view, prioritize, and submit assignments seamlessly.
•	Real-time updates, grading, reminders, and report generation.

Proposed Solution:
The proposed solution is a user-friendly platform designed to simplify assignment management for both students and teachers.
For students, the platform allows easy access to all assignments, where they can view details, set completion priorities (high, medium, or low), and filter assignments based on deadlines and status. Students can upload their completed assignments in PDF form, which will be submitted directly to the teacher for grading.
For teachers, the platform provides tools to add assignments with relevant details (subject, title, description, grades, deadline, and PDF upload). Teachers can manage and edit assignment deadlines, view student submissions, and grade them efficiently.
This solution streamlines the process of assignment tracking, submission, and grading, making the experience more organized and less time-consuming for both students and teachers.

![image](https://github.com/user-attachments/assets/12b4bf1f-ff2c-4eff-b04f-0d57141209d3)

🛠️ Setup Instructions
1. 📦 Install Django
Make sure Python is installed, then run:
pip install django

3. 🧱 Start the Django Project (if not already done)
django-admin startproject project_tracker
cd project_tracker
python manage.py startapp tracker
4. 🔧 Apply Migrations
python manage.py migrate
5. 🔑 Create a Superuser
python manage.py createsuperuser
Follow the prompts to set up a username, email, and password.

6. 🔐 Create Groups in Admin Panel
Start the development server:
python manage.py runserver
Then go to http://127.0.0.1:8000/admin/ and log in with your superuser credentials.

Inside the admin panel:
Navigate to Groups.
Create the following groups:
Faculty
Student

6. 👥 Create Users and Assign to Groups
Still inside the admin panel:
Go to Users
Add new users
Assign each user to either the Faculty or Student group depending on their role

Create models for tracking projects

Implement views and templates for Faculty and Students
