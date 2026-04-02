"""Helpers for reading announcements and joining their queues."""

import random
from fastapi import status, HTTPException
from mock_data import announcements
from .queue_service import queue_store

def get_all_announcements():
    """Return the mocked announcement dataset used by the UI."""
    return announcements

def get_announcement_by_id(id):
    """Return a copy of a single announcement enriched with UI helper fields."""
    announcements = get_all_announcements()
    for announcement in announcements:
        if announcement.get('id') == id:
            announcement = announcement.copy()
            announcement['joined'] = False
            announcement['error_message'] = None
            return announcement
    context = dict()
    context['error_message'] = "Announcement not found, please return to home page."
    return context
        
def join_queue_service(id):
    """Add a user to the in-memory queue when the announcement is live."""
    announcement = get_announcement_by_id(id)
    print(announcement)
    if announcement:
        if announcement.get('status') == "live":
            queue_length = len(queue_store[id])
            user_id = queue_length + 1
            queue_store[id].append(user_id)
            context = announcement
            context['joined'] = True
            context['queue_number'] = user_id
            context['estimated_waiting_time'] = context['queue_number'] * 2
            context['error_message'] = None
            return context
        else:
            context = dict()
            context['error_message'] = "Announcement not found, please return to home page."
    else:
        context = dict()
        context['error_message'] = "Announcement not found, please return to home page."
        return context
