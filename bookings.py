
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Booking:
    name: str
    start: datetime
    end: datetime
    #struttura della prenotazione, con nome, data di inizio e data di fine

class BookingSystem:
    def __init__(self):
        self.bookings = []
    #creato la classe BookingSystem, che inizializza una lista vuota per le prenotazioni
    def list_bookings(self):
        return self.bookings
    #metodo per elencare tutte le prenotazioni
    def add_booking(self, booking: Booking):
        if booking.start >= booking.end: 
            raise ValueError(f"Error: Booking '{booking.name}' has an invalid time range.")
        #metodo per aggiungere una prenotazione alla lista delle prenotazioni
        #controllo se la prenotazione ha un intervallo di tempo valido, altrimenti eccezione
       
        for existing_booking in self.bookings:
            if (booking.start < existing_booking.end and booking.end > existing_booking.start):
                raise ValueError(f"Error: Booking '{booking.name}' overlaps with existing booking '{existing_booking.name}'.")

        # If no overlaps, append the booking
        self.bookings.append(booking)
       
        #controllo se la prenotazione si sovrappone a una prenotazione esistente, altrimenti solleva un'eccezione
             
   
        #todo: aggiungere logica per non permettere prenotazioni prima della data odierna
        
booking_system = BookingSystem()
booking1 = Booking(name="John Doe", start=datetime(2024, 7,1, 14, 0), end=datetime(2024, 7, 1, 15, 0))
try:
    booking_system.add_booking(booking1)
except ValueError as e:
    print(e)
booking2 = Booking(name="Jane Smith", start=datetime(2024, 7, 1, 15, 0), end=datetime(2024, 7, 1, 16, 0))
try:
    booking_system.add_booking(booking2) 
except ValueError as e:
        print(e)
booking3 = Booking(name="Alice Johnson", start=datetime(2024, 7, 1, 14, 30), end=datetime(2024, 7, 1, 15, 30))
try:
    booking_system.add_booking(booking3)
except ValueError as e:
    print(e)
#prenotazioni di esempio

for booking in booking_system.list_bookings():
    if booking.start >= booking.end:
        print(f"Error: Booking '{booking.name}' has an invalid time range.")
    else:
        print(f"Booking: {booking.name}, Start: {booking.start}, End: {booking.end}")
