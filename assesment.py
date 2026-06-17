#  creare un oggetto prenotaazione, che dentro ha delle proprietà (nome, inizio e fine)
#datetime -> usare il datetime fa capire a python che il dato che stiamo inserendo è una data e non una stringa es. start = datetime(2026, 6, 17, 10, 0)
# from datetime import datetime -> perché devo fare questo passaggio? 
# per prenotazione non valida blocco if -> se la data di inizio è maggiore o uguale della data di fine, allora la prenotazione non è valida

# step lista per salvare prenotazioni: per creare una lista prima una vuota: bookings = []
#alla lista aggiungere prenotazioni con la proprietà .append ()
#per leggerle tutte ciclo for

def say_hello(name):
    return f"Ciao {name}"