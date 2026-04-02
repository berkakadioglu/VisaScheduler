# Visa Scheduler

Visa Scheduler is a FastAPI-based prototype for managing visa appointment announcements and queue participation.

It currently provides a simple server-rendered flow where users can browse announcements, view appointment details, join a live queue, and register accounts. The project is intentionally lightweight right now, with mocked announcement data and an in-memory queue, so the core scheduling flow can be built out quickly.

This project also responds to a real-world problem. In Turkey, visa appointment processes can become frustrating because of heavy demand, limited appointment availability, and system bottlenecks during queue and booking periods. Visa Scheduler is an attempt to explore how a dynamic queue-based approach could make that process more controlled, transparent, and fair for users trying to secure an appointment.

## Focus Of The Project

The main goal of this project is to evolve into a more capable queue-driven appointment system rather than remain a static listing app.

The next major feature is a dynamic queue system. That feature will be the centerpiece of the next iteration and is expected to improve the product in a few important ways:

- dynamic queue positions instead of basic in-memory ordering
- more realistic waiting-time estimates
- better handling of queue opening and closing windows
- persistent queue state
- improved support for concurrent users joining the same announcement

## Current Features

- announcement listing page
- announcement detail page
- join queue action for live announcements
- user registration endpoint
- FastAPI API documentation via Scalar

## Tech Stack

- FastAPI
- SQLModel / SQLAlchemy
- PostgreSQL
- Redis
- Jinja2
- Bootstrap

## Project Structure

```text
app/
  database/     database and Redis setup
  models/       SQLModel models
  schemas/      request and response schemas
  services/     business logic
  templates/    Jinja templates
  main.py       application entrypoint
mock_data.py    temporary announcement data
```

## Local Development

1. Create a virtual environment.
2. Install the dependencies.
3. Add the required values to `.env`.
4. Run the application.

Example:

```powershell
uvicorn app.main:app --reload
```

## Configuration

The app reads its PostgreSQL, Redis, and JWT settings from `.env` using `pydantic-settings`.

## Roadmap

- implement the dynamic queue system
- replace mocked queue behavior with persistent queue logic
- improve authentication and user flows
- add tests and stronger validation
