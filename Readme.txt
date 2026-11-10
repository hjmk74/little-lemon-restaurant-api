LITTLE LEMON - DJANGO RESTAURANT API

Project overview
Little Lemon is a Django application for a Mediterranean restaurant. It serves a restaurant home page and provides REST endpoints for menu items, table bookings, registration and token authentication. The project uses MySQL when database environment variables are configured. SQLite is used for a quick local run when DB_HOST is not set.

Requirements
- Python 3.10
- MySQL 8.x (for the MySQL configuration)
- Pipenv

Setup on Windows
1. Extract the project and open the littlelemon folder in VS Code.
2. Install dependencies:
   py -3.10 -m pip install pipenv
   py -3.10 -m pipenv install
3. Create a database in MySQL:
   CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
4. Copy .env.example to .env and enter your MySQL username and password. Keep DB_HOST set to 127.0.0.1 to use MySQL. If DB_HOST is left unset, the project uses SQLite.
5. Run migrations:
   py -3.10 -m pipenv run python manage.py migrate
6. Create an administrator:
   py -3.10 -m pipenv run python manage.py createsuperuser
7. Start the application:
   py -3.10 -m pipenv run python manage.py runserver
8. Open http://127.0.0.1:8000/

Run tests
py -3.10 -m pipenv run python manage.py test restaurant

API paths for peer review
GET    /api/menu/
POST   /api/menu/
GET    /api/menu/{id}/
PUT    /api/menu/{id}/
PATCH  /api/menu/{id}/
DELETE /api/menu/{id}/
GET    /api/bookings/
POST   /api/bookings/
GET    /api/bookings/{id}/
PUT    /api/bookings/{id}/
PATCH  /api/bookings/{id}/
DELETE /api/bookings/{id}/
POST   /api/registration/
POST   /api/token/

Authentication
Create an account with POST /api/registration/ using username, email and password. Send username and password to POST /api/token/ to receive an authentication token. For authenticated requests, add this header:
Authorization: Token your_token_value

Example booking request
POST /api/bookings/
Content-Type: application/json

{
  "name": "Alex Morgan",
  "no_of_guests": 2,
  "booking_date": "2027-01-15T18:30:00Z"
}

Menu items can be added from the Django admin or through POST /api/menu/.
