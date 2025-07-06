## 🏥 Clinikem Healthcare – Backend System
The Hospital Management System is a comprehensive web application designed to manage various aspects of hospital operations efficiently. Developed using Django, it provides functionalities for managing patient records, appointments, doctors, and administrative tasks while ensuring data security and accessibility.
This repository contains the backend system for **Clinikem Healthcare**, developed using Django. The application manages the mapping between patients and doctors and provides secure APIs for accessing patient and doctor relationships.

---

## 📌 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Setup Instructions](#setup-instructions)
- [Screenshots](#screenshots)
- [Author](#author)

---

## ✅ Features

- CRUD operations for Patients, Doctors, and their mappings
- Fetch all doctors mapped to a specific patient
- Template-based dropdown mapping interface
- REST API support with token-based authentication
- Error handling and UUID validations
- Admin panel for managing records

---

## 🧰 Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL 
- **Authentication**: DRF Token Authentication
- **Frontend (Basic)**: HTML + Django Templates (for mapping interface)

---

## 🗂️ Project Structure
├── healthcare_project/
│ ├── patients/ # App for patient models & APIs
│ ├── doctors/ # App for doctor models & APIs
│ ├── mappings/ # App for patient-doctor mapping
│ ├── manage.py
└── requirements.txt # Dependencies


---

## 🔗 API Endpoints

| Endpoint                               | Method | Description                                   |
|----------------------------------------|--------|-----------------------------------------------|
| `/api/mappings/`                       | GET    | List all patient-doctor mappings              |
| `/api/mappings/`                       | POST   | Create a new mapping                          |
| `/api/mappings/patient/<uuid>/`       | GET    | Get all doctors for a given patient UUID       |
| `/api/patients/`                       | GET    | List all patients                             |
| `/api/doctors/`                        | GET    | List all doctors                              |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/Binu-dubey/clinikem-healthcare.git
cd clinikem-healthcare

### 2. Create Virtual Environment

python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt


### 4.Run Migrations

python manage.py makemigrations
python manage.py migrate

### 5. Create Superuser (for admin access)

python manage.py createsuperuser


### 6.Start the Development Server

python manage.py runserver

## Access the site at: http://127.0.0.1:8000/

🖼️ Screenshots

![image](https://github.com/user-attachments/assets/e3593490-3fe7-445b-b2a8-ed9685bfdf5a)

![image](https://github.com/user-attachments/assets/e69595bb-162a-42b0-9d96-a95865db4332)

![image](https://github.com/user-attachments/assets/b20e6022-f158-4441-8846-fb86929a7fcb)

![image](https://github.com/user-attachments/assets/657e1f68-704a-4068-bd66-82855f71998b)



👨‍💻 Author
Binu Dubey
Backend Developer Intern Candidate
Email: [dubeybinu391@gmail.com]
GitHub: github.com/Binu-dubey





