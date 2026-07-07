# Meeting Room Booking System

## Riflessione

1. La parte piu debole della mia soluzione è che non esiste un database per inserire le prenotazioni, perciò qualsiasi modifica deve essere fatta tramite il file booking.py e non è molto intuitivo da utilizzare.

2. Con piu tempo aggiungerei dei test e ripulirei la logica ripetuta tra l'aggiunta e l'aggiornamento delle prenotazioni. Ad esempio, su update_booking ripeto i controlli che vengono fatti su add_booking. Una soluzione sarebbe richiamare quei controlli senza doverli riscrivere.

3. Il livello che mi ha costretto a ripensare di piu la soluzione è stato il primo, in quanto la difficoltà maggiore che ho riscontrato è stata proprio quella di scrivere codice da zero su un file vuoto.

4. Ho deciso di non gestire aspetti come database, autenticazione, prenotazioni ricorrenti, fusi orari o una vera interfaccia utente. Penso sia stata la scelta giusta perche l'obiettivo del progetto è mostrare chiaramente la logica principale delle prenotazioni, non costruire un sistema completo da produzione.

5. Il problema nel caso in cui due utenti inserissero una prenotazione nello stesso momento esisterebbe nel caso in cui non ci fosse una gerarchia. Il problema si potrebbe contenere in primo luogo stabilendo una gerarchia di utenti. Nel caso in cui invece, due utenti di stesso grado inseriscono due prenotazioni in overlap, nessuna delle due viene inserita e viene dato un feedback a entrambi con il motivo del mancato inserimento.
