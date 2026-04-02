"""Temporary in-memory seed data for the prototype application."""

import datetime

announcements = [
    {
        "title": "Announcement 1",
        "id": 1,
        "queue_open_at": datetime.datetime(2026, 3, 20, 10, 0, 0),
        "reservation_open_at": datetime.datetime(2026, 3, 20, 12, 0, 0),
        "appointment_date": datetime.date(2026, 3, 27),
        "slots": 11,
        "status": "open"
    },
    {
        "title": "Announcement 2",
        "id": 2,
        "queue_open_at": datetime.datetime(2026, 3, 20, 14, 0, 0),
        "reservation_open_at": datetime.datetime(2026, 3, 20, 16, 0, 0),
        "appointment_date": datetime.date(2026, 3, 28),
        "slots": 4,
        "status": "closed",
    },
    {
        "title": "Announcement 3",
        "id": 3,
        "queue_open_at": datetime.datetime(2026, 3, 21, 10, 0, 0),
        "reservation_open_at": datetime.datetime(2026, 3, 21, 12, 0, 0),
        "appointment_date": datetime.date(2026, 3, 29),
        "slots": 14,
        "status": "live"
    },
    {
        "title": "Announcement 4",
        "id": 4,
        "queue_open_at": datetime.datetime(2026, 3, 21, 14, 0, 0),
        "reservation_open_at": datetime.datetime(2026, 3, 21, 16, 0, 0),
        "appointment_date": datetime.date(2026, 3, 30),
        "slots": 7,
        "status": "live"
    },

]
