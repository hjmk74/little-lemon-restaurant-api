# Little Lemon Restaurant API

A restaurant management web application built with Django and Django REST Framework. The project provides restaurant menu management, table booking functionality, user registration, and token-based authentication, with MySQL database integration.

## Features

- **Restaurant Menu:** View, create, update, and delete menu items.
- **Table Booking:** Create and view restaurant reservations.
- **User Registration:** Register new user accounts.
- **Token Authentication:** Obtain authentication tokens through the API.
- **Data Validation:** Validate reservation dates and time slots.
- **Django Admin:** Manage application data through the Django administration interface.
- **Automated Testing:** 11 tests covering the main application and API functionality.

## Technology Stack

- Python 3.10
- Django
- Django REST Framework
- MySQL
- Django REST Framework Token Authentication
- Pipenv

## Project Structure

```text
littlelemon/
├── littlelemon/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── restaurant/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── api_urls.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── .env.example
├── .gitignore
├── manage.py
├── Pipfile
├── Pipfile.lock
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/hjmk74/little-lemon-restaurant-api.git
cd little-lemon-restaurant-api
```

### 2. Install dependencies

```bash
pip install pipenv
pipenv install
```

### 3. Configure environment variables

Create a `.env` file in the project root using `.env.example` as a reference.

Configure your Django settings and MySQL database credentials in the local `.env` file.

Do not commit your `.env` file or expose database passwords and secret keys.

### 4. Apply database migrations

```bash
pipenv run python manage.py migrate
```

### 5. Start the development server

```bash
pipenv run python manage.py runserver
```

Open the application at:

http://127.0.0.1:8000/

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/menu/` | Retrieve all menu items |
| POST | `/api/menu/` | Create a menu item |
| GET | `/api/menu/{id}/` | Retrieve a menu item by ID |
| PUT/PATCH | `/api/menu/{id}/` | Update a menu item |
| DELETE | `/api/menu/{id}/` | Delete a menu item |
| GET | `/api/bookings/` | Retrieve restaurant bookings |
| POST | `/api/bookings/` | Create a restaurant booking |
| POST | `/api/registration/` | Register a new user |
| POST | `/api/token/` | Obtain an authentication token |

## Authentication

The project includes Django REST Framework Token Authentication.

The token endpoint accepts a username and password and returns an authentication token for valid credentials.

For authenticated API requests, use the following HTTP header:

```http
Authorization: Token YOUR_AUTH_TOKEN
```

## Database

The project is configured to use MySQL through environment variables.

SQLite is also configured as a fallback when no MySQL host is provided.

## Running Tests

Run the restaurant application tests using:

```bash
pipenv run python manage.py test restaurant
```

**Latest test result:** 11 tests passed successfully.

## Project Purpose

This project was developed as part of the Meta Back-End Developer Professional Certificate capstone work, demonstrating Django application development, REST API implementation, database integration, user registration, and automated testing.
