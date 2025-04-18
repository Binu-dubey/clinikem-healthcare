# Healthcare Backend API

A robust backend system for a healthcare application built with Django, Django REST Framework (DRF), and PostgreSQL.

## Features

- User authentication with JWT tokens
- Patient management
- Doctor management
- Patient-Doctor relationship mapping
- Secure PostgreSQL database storage
- RESTful API architecture

## Tech Stack

- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication (djangorestframework-simplejwt)

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/healthcare-backend.git
   cd healthcare-backend
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables
   Create a `.env` file in the project root with the following variables:
   ```
   DB_NAME=healthcare_db
   DB_USER=postgres
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   SECRET_KEY=your_django_secret_key
   ```

5. Run migrations
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser (optional)
   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server
   ```bash
   python manage.py runserver
   ```

## API Documentation

### Authentication APIs

#### Register a new user
- **URL**: `POST /api/auth/register/`
- **Description**: Register a new user with name, email, and password
- **Request Body**:
  ```json
  {
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword",
    "first_name": "John",
    "last_name": "Doe"
  }
  ```
- **Response**: 
  ```json
  {
    "refresh": "jwt_refresh_token",
    "access": "jwt_access_token",
    "user": {
      "id": 1,
      "username": "john_doe",
      "email": "john@example.com",
      "first_name": "John",
      "last_name": "Doe"
    }
  }
  ```

#### Login a user
- **URL**: `POST /api/auth/login/`
- **Description**: Log in a user and return a JWT token
- **Request Body**:
  ```json
  {
    "username": "john_doe",
    "password": "securepassword"
  }
  ```
- **Response**:
  ```json
  {
    "refresh": "jwt_refresh_token",
    "access": "jwt_access_token"
  }
  ```

### Patient Management APIs

#### Add a new patient
- **URL**: `POST /api/patients/`
- **Authentication**: JWT token required
- **Description**: Add a new patient (Authenticated users only)
- **Request Body**:
  ```json
  {
    "first_name": "Alice",
    "last_name": "Smith",
    "date_of_birth": "1990-01-15",
    "gender": "F",
    "contact_number": "555-123-4567",
    "address": "123 Health St, Medical City, MC 12345",
    "medical_history": "Allergic to penicillin"
  }
  ```
- **Response**: Patient object with ID

#### Retrieve all patients
- **URL**: `GET /api/patients/`
- **Authentication**: JWT token required
- **Description**: Retrieve all patients created by the authenticated user
- **Response**: Array of patient objects

#### Get a specific patient
- **URL**: `GET /api/patients/{id}/`
- **Authentication**: JWT token required
- **Description**: Get details of a specific patient
- **Response**: Patient object

#### Update a patient
- **URL**: `PUT /api/patients/{id}/`
- **Authentication**: JWT token required
- **Description**: Update patient details
- **Request Body**: Patient fields to update
- **Response**: Updated patient object

#### Delete a patient
- **URL**: `DELETE /api/patients/{id}/`
- **Authentication**: JWT token required
- **Description**: Delete a patient record
- **Response**: 204 No Content

### Doctor Management APIs

#### Add a new doctor
- **URL**: `POST /api/doctors/`
- **Authentication**: JWT token required
- **Description**: Add a new doctor (Authenticated users only)
- **Request Body**:
  ```json
  {
    "first_name": "Robert",
    "last_name": "Johnson",
    "specialization": "Cardiology",
    "license_number": "MED12345",
    "contact_number": "555-987-6543",
    "email": "dr.robert@hospital.com",
    "years_of_experience": 15
  }
  ```
- **Response**: Doctor object with ID

#### Retrieve all doctors
- **URL**: `GET /api/doctors/`
- **Authentication**: JWT token required
- **Description**: Retrieve all doctors
- **Response**: Array of doctor objects

#### Get a specific doctor
- **URL**: `GET /api/doctors/{id}/`
- **Authentication**: JWT token required
- **Description**: Get details of a specific doctor
- **Response**: Doctor object

#### Update a doctor
- **URL**: `PUT /api/doctors/{id}/`
- **Authentication**: JWT token required
- **Description**: Update doctor details
- **Request Body**: Doctor fields to update
- **Response**: Updated doctor object

#### Delete a doctor
- **URL**: `DELETE /api/doctors/{id}/`
- **Authentication**: JWT token required
- **Description**: Delete a doctor record
- **Response**: 204 No Content

### Patient-Doctor Mapping APIs

#### Assign a doctor to a patient
- **URL**: `POST /api/mappings/`
- **Authentication**: JWT token required
- **Description**: Assign a doctor to a patient
- **Request Body**:
  ```json
  {
    "patient": 1,
    "doctor": 2,
    "notes": "Primary care physician"
  }
  ```
- **Response**: Mapping object with ID

#### Retrieve all patient-doctor mappings
- **URL**: `GET /api/mappings/`
- **Authentication**: JWT token required
- **Description**: Retrieve all patient-doctor mappings
- **Response**: Array of mapping objects

#### Get all doctors for a specific patient
- **URL**: `GET /api/mappings/patient/{patient_id}/`
- **Authentication**: JWT token required
- **Description**: Get all doctors assigned to a specific patient
- **Response**: Array of mapping objects with doctor details

#### Get all patients for a specific doctor
- **URL**: `GET /api/mappings/doctor/{doctor_id}/`
- **Authentication**: JWT token required
- **Description**: Get all patients assigned to a specific doctor
- **Response**: Array of mapping objects with doctor details

#### Remove a doctor from a patient
- **URL**: `DELETE /api/mappings/{id}/`
- **Authentication**: JWT token required
- **Description**: Remove a doctor from a patient
- **Response**: 204 No Content

## Error Handling

All API endpoints include appropriate error handling:

- **400 Bad Request**: For invalid input data
- **401 Unauthorized**: For authentication issues
- **403 Forbidden**: For permission issues
- **404 Not Found**: For resources that don't exist
- **500 Internal Server Error**: For server-side errors

Each error response includes an appropriate message explaining the issue.

## Data Models

### Patient
- user (Foreign Key to User)
- first_name (CharField)
- last_name (CharField)
- date_of_birth (DateField)
- gender (CharField with choices)
- contact_number (CharField)
- address (TextField)
- medical_history (TextField, optional)
- created_at (DateTimeField, auto-generated)
- updated_at (DateTimeField, auto-updated)

### Doctor
- first_name (CharField)
- last_name (CharField)
- specialization (CharField)
- license_number (CharField, unique)
- contact_number (CharField)
- email (EmailField, unique)
- years_of_experience (PositiveIntegerField)
- created_at (DateTimeField, auto-generated)
- updated_at (DateTimeField, auto-updated)

### PatientDoctorMapping
- patient (Foreign Key to Patient)
- doctor (Foreign Key to Doctor)
- assigned_date (DateTimeField, auto-generated)
- notes (TextField, optional)

## Security Considerations

- JWT tokens expire after 1 hour (configurable)
- Refresh tokens are valid for 1 day (configurable)
- All sensitive data is stored in environment variables
- PostgreSQL provides robust data storage
- All API endpoints requiring authentication are protected
