from datetime import datetime
from dataclasses import dataclass
from booking_system import Booking, BookingSystem

booking_system = BookingSystem()

bookings = [
    Booking(name="John Doe", room="A", start=datetime(2024, 6, 1, 14, 0), end=datetime(2024, 6, 1, 16, 0), id=1),
    Booking(name="Jane Smith", room="A", start=datetime(2024, 6, 1, 15, 0), end=datetime(2024, 6, 1, 17, 0), id=2),
    Booking(name="Alice Johnson", room="B", start=datetime(2027, 6, 2, 10, 0), end=datetime(2027, 6, 2, 12, 0), id=3),
    Booking(name="Bob Brown", room="B", start=datetime(2026, 8, 2, 11, 0), end=datetime(2026, 8, 2, 13, 0), id=4),
    Booking(name="Brother Johnson", room="B", start=datetime(2027, 7, 2, 10, 0), end=datetime(2027, 7, 2, 12, 0), id=3),
]

for booking in bookings:
    try:
        booking_system.add_booking(booking)
    except ValueError as e:
        print(e)
 
updates = [
    (4, "Bob Brown Updated", "B", datetime(2027, 6, 2, 10, 0), datetime(2027, 6, 2, 12, 0))
 ]

for update in updates:
    try:
        booking_system.update_booking(*update)
    except ValueError as e:
        print(e)

booking_system.remove_booking(4)




for booking in booking_system.list_bookings():
    print(f"Booking ID: {booking.id}, Name: {booking.name}, Room: {booking.room}, Start: {booking.start}, End: {booking.end}")
    



searches = [
    ("A", datetime(2024, 6, 1)),
    ("B", datetime(2027, 6, 2)),
]


for room, date in searches:
    available_slots = booking_system.find_available_slots(room, date)
    for start, end in available_slots:
        print(f"Available slots for room {room} on date {date.date()}: Start: {start}, End: {end}")

