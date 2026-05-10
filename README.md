Django Photo Sharing App

A backend-oriented photo sharing web application built using Django.
Users can register, log in, upload memories with images, like posts, and delete only their own posts.

The project focuses on:
* Django backend development
* Authentication & authorization
* File uploads
* CRUD operations
* ORM optimization
* Template rendering
* Bootstrap UI
-------------------------------------
Features:

* User Registration
* User Login & Logout
* Password Validation
* Upload Photo Memories
* Like / Unlike Posts
* Delete Own Posts
* Django Messages Framework
* Image Upload Support
* Bootstrap UI
* Authentication Protection
* ORM Optimization using:
   * select_related
   * prefetch_related
-------------------------------------------     
Tech Stack: 

Python
Django
Bootstrap 5
SQLite
HTML Templates
------------------------------------------
Project Structure :

django-photo-sharing-app/
│
├── memories/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── feed.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── create_post.html
│   │
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── serializers.py
│
├── media/
├── static/
├── memory_project/
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
----------------------------------------------
Database Model: 

MemoryPost Model:

class MemoryPost(models.Model):

    user = models.ForeignKey(User)

    image = models.ImageField()

    description = models.TextField()

    likes = models.ManyToManyField(User)

    created_at = models.DateTimeField()
----------------------------------------------    
Authentication Features:

The project uses Django Authentication System:

authenticate()
login()
logout()
@login_required

Users must log in to:

upload posts
like posts
delete posts
---------------------------------------------
Password Validation Rules:

Password must contain:

Minimum 8 characters
Maximum 12 characters
One uppercase letter
One lowercase letter
One number
One special character

Example:  Admin@123
--------------------------------------------
Installation

Clone Repository
git clone https://github.com/your-username/django-photo-sharing-app.git

Navigate to Project:
cd django-photo-sharing-app

Create Virtual Environment:
python -m venv venv

Activate Virtual Environment:
Windows
venv\Scripts\activate

Linux / Mac
source venv/bin/activate
--------------------------------------------
Install Dependencies:
pip install -r requirements.txt
--------------------------------------------
Run Migrations:
python manage.py makemigrations
python manage.py migrate
--------------------------------------------
Run Server:
python manage.py runserver
--------------------------------------------
Open in Browser
http://127.0.0.1:8000/
---------------------------------------------
Screenshots

Add screenshots here after deployment.

Example:

screenshots/feed-page.png
screenshots/login-page.png
screenshots/upload-page.png
--------------------------------------------
Future Improvements:

Comment System
Profile Pictures
Edit Posts
Search Feature
Pagination
REST API Integration
JWT Authentication
Cloud Image Storage
Docker Deployment

--------------------------------------------
Learning Outcomes

This project helped in understanding:

Django Models
Views & Templates
Authentication & Authorization
File Upload Handling
Query Optimization
Bootstrap Integration
CRUD Operations
Messages Framework
Backend Architecture
----------------------------------------------
Author :
Srinjay Kumar

Django Developer
Python Developer
Backend Developer
----------------------------------------------
License :
This project is for learning and educational purposes.
