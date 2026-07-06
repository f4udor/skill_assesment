from datetime import datetime
from dataclasses import dataclass
from booking_system import Booking, BookingSystem

booking_system = BookingSystem()
booking1 = Booking(name="John Doe", start=datetime(2024, 7,1, 14, 0), end=datetime(2024, 7, 1, 15, 0), id=1)
try:
    booking_system.add_booking(booking1)
except ValueError as e:
    print(e)
booking2 = Booking(name="Jane Smith", start=datetime(2024, 7, 1, 15, 0), end=datetime(2024, 7, 1, 16, 0), id=2)
try:
    booking_system.add_booking(booking2) 
except ValueError as e:
    print(e)
booking3 = Booking(name="Alice Johnson", start=datetime(2024, 7, 1, 14, 30), end=datetime(2024, 7, 1, 15, 30), id=3)
try:
    booking_system.add_booking(booking3)
except ValueError as e:
    print(e)
booking4 = Booking(name="Bob Brown", start=datetime(2027, 6, 30, 14, 0), end=datetime(2027, 6, 30, 15, 0), id=4)
try:
    booking_system.add_booking(booking4)
except ValueError as e:
    print(e)
booking5 = Booking(name="Charlie Davis", start=datetime(2027, 7, 1, 12, 0), end=datetime(2027, 7, 1, 14, 0), id=5)
try:
    booking_system.add_booking(booking5)
except ValueError as e:
    print(e)
    
    remove_booking_id = 4
    try:
        booking_system.remove_booking(remove_booking_id)
    except ValueError as e:
        print(e)
        
update_booking_id = 5
new_name = "Charlie Davis Updated"
try:
    booking_system.update_booking(update_booking_id, new_name, None, None)
except ValueError as e:
    print(e)
        
for booking in booking_system.list_bookings():
    if booking.start >= booking.end:
        print(f"Error: Booking '{booking.name}' has an invalid time range.")
    else:
        print(f"Booking: {booking.name}, Start: {booking.start}, End: {booking.end}")
#prenotazioni di esempio