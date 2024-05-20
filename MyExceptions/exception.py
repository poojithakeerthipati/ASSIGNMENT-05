class EventNotFoundException(Exception):
    def __init__(self, event_id):
        super().__init__(f"Event with ID {event_id} is not found")


class InvalidBookingIDException(Exception):
    def __init__(self, booking_id):
        super().__init__(f"Invalid booking ID: {booking_id}")
