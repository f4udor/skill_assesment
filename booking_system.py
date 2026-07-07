
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Booking:
    name: str
    room: str
    start: datetime
    end: datetime
    id: int
   
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
            if existing_booking.room == booking.room:
                if (booking.start < existing_booking.end and booking.end > existing_booking.start):
                    raise ValueError(f"Error: Booking '{booking.name}' overlaps with existing booking '{existing_booking.name}'.")
        self.bookings.append(booking)
        
    def remove_booking(self, booking_id: int):
        for booking in self.bookings:
            if booking_id == booking.id:
                self.bookings.remove(booking)
                print(f"Booking with ID '{booking_id}' has been removed.")
                
            else:
                raise ValueError(f"Error: Booking with ID '{booking_id}' not found.")
                
    def update_booking(self, booking_id:int, new_name: str, new_room: str, new_start: datetime, new_end: datetime):
        for booking in self.bookings:
            if booking.id == booking_id:
                final_name = new_name if new_name is not None else booking.name
                final_room = new_room if new_room is not None else booking.room
                final_start = new_start if new_start is not None else booking.start
                final_end = new_end if new_end is not None else booking.end

                if final_start < datetime.now() or final_end < datetime.now():
                    raise ValueError(f"Error: Updated booking '{final_name}' cannot be made for a past date.")
                if final_start >= final_end:
                    raise ValueError(f"Error: Updated booking '{final_name}' has an invalid time range.")
                
                for existing_booking in self.bookings:
                     if existing_booking.room == final.room:   
                        if existing_booking.id != booking_id and (final_start < existing_booking.end and final_end > existing_booking.start):
                            raise ValueError(f"Error: Updated booking '{final_name}' overlaps with existing booking '{existing_booking.name}'.")

                booking.name = final_name
                booking.room = final_room
                booking.start = final_start
                booking.end = final_end
                
                print(f"Booking with ID '{booking_id}' has been updated.")
                return
        raise ValueError(f"Error: Booking with ID '{booking_id}' not found.")


