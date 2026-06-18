
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


    
    