from booking import Booking
    
class BookingSystem:
    def __init__(self):
         self.bookings = []
    #creato la classe BookingSystem, che inizializza una lista vuota per le prenotazioni
    def list_bookings(self):
        return self.bookings
    #metodo per elencare tutte le prenotazioni
    def add_booking(self, booking: Booking):
        self.bookings.append(booking)
    #metodo per aggiungere una prenotazione alla lista delle prenotazioni
    

