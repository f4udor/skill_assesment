
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Booking:
    name: str
    start: datetime
    end: datetime
    id: int
    #mettere id, per identificare univocamente la prenotazione, e facilitare operazioni di aggiornamento e cancellazione
    #struttura della prenotazione, con nome, data di inizio e data di fine

class BookingSystem:
    def __init__(self):
        self.bookings = []
    #creato la classe BookingSystem, che inizializza una lista vuota per le prenotazioni
    def list_bookings(self):
        return self.bookings
    #metodo per elencare tutte le prenotazioni
    def add_booking(self, booking: Booking):
        if (booking.start < datetime.now() or booking.end < datetime.now()):
            raise ValueError(f"Error: Booking '{booking.name}' cannot be made for a past date.")
        if booking.start >= booking.end: 
            raise ValueError(f"Error: Booking '{booking.name}' has an invalid time range.")
        for existing_booking in self.bookings:
            if (booking.start < existing_booking.end and booking.end > existing_booking.start):
                raise ValueError(f"Error: Booking '{booking.name}' overlaps with existing booking '{existing_booking.name}'.")
        self.bookings.append(booking)
        
    def remove_booking(self, booking_id: int):
        for booking in self.bookings:
            if booking_id == booking.id:
                self.bookings.remove(booking)
                print(f"Booking with ID '{booking_id}' has been removed.")
                return
            else:
                raise ValueError(f"Error: Booking with ID '{booking_id}' not found.")
                
        

            #implementare logica x aggiornare prenotazione
            


