# beneficiary_app
This Django-based application is designed to facilitate beneficiary registration and management of cash transfers for assistance projects. 
The application allows the registration of households, their members, and enrollment in specific assistance projects, along with the generation of CSV file summaries.

##Features

Registration and management of households
Addition of household members with relevant details
Creation and management of assistance projects
Enrollment of households in assistance projects with cash offers
Django Admin interface for easy management and CRUD operations
Django management commands for automated tasks

##Requirements

Python 3.7+
Django 3+

##Usage
Create projects: python manage.py createprojects
This command creates 5 projects in the application.
Create households: python manage.py createhouseholds
This command creates 10 households with at least 5 members in each.
Enroll households: python manage.py enrollhouseholds
This command enlists 3 households in an assistance project with a $100 cash offer.
Extract CSV file summary: python manage.py exportenrollments
This command exports a CSV file summarizing enrollments in the assistance project, including enrollment ID, household ID, household name, household recipient's full name, cash offer, and phone number.

##Django Admin


Access the Django Admin interface by running the development server: python manage.py runserver
Open the browser and navigate to http://localhost:8000/admin/
Log in with your superuser credentials to access the admin dashboard.
Username Admin Password Tech:1990
Perform CRUD operations on households, persons, assistance projects, and enrollments.
