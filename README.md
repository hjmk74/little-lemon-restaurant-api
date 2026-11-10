# Little Lemon - Django Restaurant API

## Project Overview

Little Lemon is a Django application for a Mediterranean restaurant. It serves a restaurant home page and provides REST API endpoints for menu items, table bookings, user registration, and token authentication.

The project uses MySQL when database environment variables are configured. SQLite is used as a local fallback when `DB_HOST` is not set.

## Requirements

- Python 3.10
- MySQL 8.x (for the MySQL configuration)
- Pipenv

## Technology Stack

- Python 3.10
- Django
- Django REST Framework
- MySQL
- Django REST Framework Token Authentication
- Pipenv

## Features

- Restaurant home page
- Menu item listing and management
- Table booking endpoints
- User registration
- Token authentication
- Booking date and reservation slot validation
- Django administration interface
- Automated tests

## Setup on Windows

### 1. Open the project

Extract or clone the repository, then open the project folder containing `manage.py` in VS Code.

### 2. Install Pipenv and project dependencies

```powershell
py -3.10 -m pip install pipenv
py -3.10 -m pipenv install
```

### 3. Configure the database

For MySQL, create the database:

```sql
CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Copy `.env.example` to `.env` and enter your local Django and MySQL settings. Keep `DB_HOST=127.0.0.1` to use MySQL. If `DB_HOST` is not set, the project uses SQLite.

Never commit your real `.env` file or share database passwords and secret keys.

### 4. Run database migrations

```powershell
py -3.10 -m pipenv run python manage.py migrate
```

### 5. Create an administrator (optional)

```powershell
py -3.10 -m pipenv run python manage.py createsuperuser
```

### 6. Start the development server

```powershell
py -3.10 -m pipenv run python manage.py runserver
```

Open the application at:

http://127.0.0.1:8000/

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/menu/` | List menu items |
| POST | `/api/menu/` | Create a menu item |
| GET | `/api/menu/{id}/` | Retrieve a menu item |
| PUT | `/api/menu/{id}/` | Replace a menu item |
| PATCH | `/api/menu/{id}/` | Partially update a menu item |
| DELETE | `/api/menu/{id}/` | Delete a menu item |
| GET | `/api/bookings/` | List bookings |
| POST | `/api/bookings/` | Create a booking |
| GET | `/api/bookings/{id}/` | Retrieve a booking |
| PUT/PATCH | `/api/bookings/{id}/` | Update a booking |
| DELETE | `/api/bookings/{id}/` | Delete a booking |
| POST | `/api/registration/` | Register a user |
| POST | `/api/token/` | Obtain an authentication token |

## Example Booking Request

```http
POST /api/bookings/
Content-Type: application/json
```

```json
{
  "first_name": "Alex Morgan",
  "reservation_date": "2026-11-15",
  "reservation_slot": 14
}
```

Use a current or future date and a reservation slot between 10 and 20.

## Authentication

Register an account using `POST /api/registration/` with a username, email, and password.

Send the username and password to `POST /api/token/` to obtain an authentication token.

For authenticated API requests, include this HTTP header:

```http
Authorization: Token YOUR_AUTH_TOKEN
```

## Django Admin

Menu items and bookings can also be managed through the Django administration interface at:

http://127.0.0.1:8000/admin/

Create an administrator account using the `createsuperuser` command described above.

## Running Tests

Run the restaurant application test suite:

```powershell
py -3.10 -m pipenv run python manage.py test restaurant
```

The current test suite contains 11 tests. The latest local test run completed successfully with all 11 tests passing.

## Project Purpose

This project was developed as part of the Meta Back-End Developer Professional Certificate capstone work. It demonstrates Django application development, REST API implementation, database integration, user registration, token authentication, and automated testing.
