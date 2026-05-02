# NotifyMe Backend

A Django REST API for user signup/authentication and booking creation with asynchronous confirmation emails. This project demonstrates a clean backend foundation using JWT auth, PostgreSQL, Celery workers, and RabbitMQ.

## Portfolio Highlights

- **Custom user model** with email-based login.
- **JWT authentication** using access/refresh tokens.
- **Protected API endpoints** with DRF permission classes.
- **Booking workflow** that generates unique references.
- **Async task processing** with Celery + RabbitMQ.
- **Containerized development** with Docker Compose.

## Tech Stack

- Python 3.11
- Django + Django REST Framework
- PostgreSQL
- Celery
- RabbitMQ
- SimpleJWT
- Docker / Docker Compose

## API Features

### Authentication & Users

- `POST /api/users/signup/` — create a user account
- `POST /api/token/` — get JWT access/refresh tokens
- `POST /api/token/refresh/` — refresh access token
- `GET /api/users/me/` — return the current authenticated user

### Bookings

- `POST /api/bookings/create/` — create a booking for the authenticated user
  - Automatically generates a UUID reference
  - Triggers an async booking confirmation email task

## Local Setup

### 1) Prerequisites

- Docker + Docker Compose
- Or local Python/PostgreSQL/RabbitMQ setup (if not using Docker)

### 2) Environment variables

Create a `.env` file in the project root:

```env
DB_NAME=notifyme
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### 3) Start with Docker Compose

```bash
docker compose up --build
```

The API will be available at `http://localhost:8000`.

### 4) Run migrations

In a separate terminal:

```bash
docker compose exec web python manage.py migrate
```

## Example API Flow

1. Sign up:

```http
POST /api/users/signup/
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "strong-password"
}
```

2. Obtain JWT token pair:

```http
POST /api/token/
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "strong-password"
}
```

3. Create a booking (authenticated):

```http
POST /api/bookings/create/
Authorization: Bearer <access_token>
```

## Project Structure

```text
config/      # Django project settings, URLs, ASGI/WSGI, Celery app
users/       # Custom user model, signup + current-user endpoints
bookings/    # Booking model, serializer, API view, Celery email task
```

## Notes

- Email sending is configured to the **console backend** in development.
- Celery broker is configured for RabbitMQ (`amqp://guest:guest@rabbitmq:5672//`).
- Default REST permissions require authentication unless explicitly overridden.

## Why this project fits a portfolio

This backend demonstrates practical API engineering patterns often used in production systems: auth boundaries, async workflows, task queues, relational data modeling, and reproducible containerized environments.
