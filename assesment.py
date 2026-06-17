#  creare un oggetto prenotaazione, che dentro ha delle proprietà (nome, inizio e fine)
#datetime -> usare il datetime fa capire a python che il dato che stiamo inserendo è una data e non una stringa es. start = datetime(2026, 6, 17, 10, 0)
# from datetime import datetime -> perché devo fare questo passaggio? 
# per prenotazione non valida blocco if -> se la data di inizio è maggiore o uguale della data di fine, allora la prenotazione non è valida

# step lista per salvare prenotazioni: per creare una lista prima una vuota: bookings = []
#alla lista aggiungere prenotazioni con la proprietà .append ()
#per leggerle tutte ciclo for

# creare un bookin system che gestisce tuttie le prenotazioni. un booking è una singola prenotazione.


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