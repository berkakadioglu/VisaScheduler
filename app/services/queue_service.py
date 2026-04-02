"""In-memory queue state used by announcement flows."""

from mock_data import announcements

queue_store = dict()

async def queue_store_init():
    """Prepare an empty queue list for every mocked announcement."""
    for announcement in announcements:
        queue_store[announcement['id']] = list()

