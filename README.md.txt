# 🏥 Healthcare Backend Project

This is a simple backend system for a healthcare application built using Django, Django REST Framework, and PostgreSQL. The project allows users to register, log in, and manage patients, doctors, and their assignments. 
---

## 📦 Features

- User registration and login with JWT tokens
- CRUD APIs for Patients and Doctors
- Assign doctors to patients
- View mappings between patients and doctors
- Protected endpoints (only logged-in users can manage patients/doctors)
- PostgreSQL used as the database
- Environment variables for sensitive config

---

## 🛠️ Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- PostgreSQL
- djangorestframework-simplejwt (for JWT Auth)
- Postman (for testing)

---

## 🚀 How to Run This Project

1. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows

2. Install the Dependencies
pip install -r requirements.txt

3. Setup the Database
CREATE DATABASE healthcare_db;

Update the .env file with your DB credentials:

DB_NAME=healthcare_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

4. Run Migrations
python manage.py makemigrations
python manage.py migrate

5. Run the Server
python manage.py runserver

Server will start at: http://127.0.0.1:8000/

## 📮 API Endpoints

🔐 Auth
POST /api/auth/register/ – Register

POST /api/auth/login/ – Login and get tokens

POST /api/auth/refresh/ – Refresh access token

👤 Patients
POST /api/patients/ – Add new patient

GET /api/patients/ – List your patients

GET /api/patients/<id>/ – View patient

PUT /api/patients/<id>/ – Update patient

DELETE /api/patients/<id>/ – Delete patient

🩺 Doctors
POST /api/doctors/ – Add doctor

GET /api/doctors/ – List all doctors

GET /api/doctors/<id>/ – View doctor

PUT /api/doctors/<id>/ – Update doctor

DELETE /api/doctors/<id>/ – Delete doctor

🔗 Mappings
POST /api/mappings/ – Assign doctor to patient

GET /api/mappings/ – All mappings

GET /api/mappings/<patient_id>/ – Get doctors for a patient

DELETE /api/mappings/delete/<id>/ – Remove mapping

🧪 Testing with Postman
I've also included a Postman collection (HealthcareBackend.postman_collection.json). You can import it into Postman and test all the endpoints.

Don’t forget to add the Authorization header as: Bearer <your_access_token>

📧 Contact
If you want to suggest improvements or have any issues, feel free to reach out to me 😄

📩 Email: mdaliraza92@gmail.com

💼 LinkedIn: linkedin.com/in/mdaliraza1

📱 Phone: +91-9804921119