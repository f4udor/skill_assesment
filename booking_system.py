
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
                update_fields = {
                    "name": new_name,
                    "room": new_room,
                    "start": new_start,
                    "end": new_end
                }
                final_fields = {}
                for field_name, new_value in update_fields.items():
                    final_fields[field_name] = new_value if new_value is not None else getattr(booking, field_name)

                # todo: pulire le duplicazioni in modo da non dover aggiungere final_name = new_name if new_name

                if final_fields["start"] < datetime.now() or final_fields["end"] < datetime.now():
                    raise ValueError(f"Error: Updated booking '{final_fields['name']}' cannot be made for a past date.")
                if final_fields["start"] >= final_fields["end"]:
                    raise ValueError(f"Error: Updated booking '{final_fields['name']}' has an invalid time range.")

                for existing_booking in self.bookings:
                     if existing_booking.room == final_fields["room"]:   
                        if existing_booking.id != booking_id and (final_fields["start"] < existing_booking.end and final_fields["end"] > existing_booking.start):
                            raise ValueError(f"Error: Updated booking '{final_fields['name']}' overlaps with existing booking '{existing_booking.name}'.")

                for field_name, new_value in final_fields.items():
                    setattr(booking, field_name, new_value)
                
                print(f"Booking with ID '{booking_id}' has been updated.")
                return
        raise ValueError(f"Error: Booking with ID '{booking_id}' not found.")
    
    def find_avaible_slots(self, room: str, date: datetime):
        slots = []
        start_of_day = datetime(date.year, date.month, date.day, 0, 0)
        end_of_day = datetime(date.year, date.month, date.day, 23, 59)
        current_time = start_of_day


       


