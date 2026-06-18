from datetime import datetime
from system import BookingSystem
from booking import Booking

booking_system = BookingSystem()
booking1 = Booking(name="John Doe", start=datetime(2024, 7,1, 14, 0), end=datetime(2024, 7, 1, 15, 0))