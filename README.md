# File Organizer - Python/Numpy

Progetto Start2Impact per la creazione di un prompt in linguaggio Python per l'organizzazione di file in base all'estensione.


Il progetto è stato svolto in base alle conoscenze acquisite sulla programmazione in linguaggio Python e sull'utilizzo della libreria Numpy.


#
Nella cartella files trovi 8 file:

  - 2 file di testo
  - 2 file audio
  - 4 immagini, con varie estensioni.

## Step #1

Inizia creando, in un notebook, uno script Python che iteri in ordine alfabetico sui file della cartella files e, a seconda del tipo (audio, documento, immagine), li sposti nella relativa sottocartella (qui sotto trovi un esempio). Se la sottocartella non esiste, il tuo script dovrà crearla automaticamente.

Durante il ciclo, lo script deve stampare le informazioni dei file: nome, tipo e dimensione in byte. Questo è l'output desiderato:

bw type:image size:94926B


ciao type:doc size:12B 


daffodil type:image size:24657B


eclipse type:image size:64243B


pippo type:doc size:8299B


song1 type:audio size:1087849B


song2 type:audio size:764176B


trump type:image size:10195B

<br>

Oltre a stamparne le informazioni via via che li sposti, tieni traccia dei file creando un documento recap.csv con le stesse informazioni. Trovi un esempio in questa cartella.

La struttura finale della cartella files dovrà essere:

    - files            
        - audio
            - song1.mp3
            - song2.mp3
        - docs
            - ciao.txt
            - pippo.odt
        - images
            - bw.png
            - daffodil.jpg
            - eclipse.png
            - trump.jpeg    
        - recap.csv
<br>
Commenta il codice con i passaggi che fai. Questo vale anche per i prossimi Step.

Attenzione: lo script, ogni volta che viene lanciato per spostare nuovi file, deve aggiornare (e non sovrascrivere) le sottocartelle e il file di recap. Per controllare che tutto funzioni correttamente, puoi aggiungere altri file alla cartella files e fare un test; oppure, puoi dividere gli 8 file originali in due gruppi e lasciarne uno per il test.


## Step #2

Inserisci lo script che hai creato in un piccolo eseguibile (chiamalo addfile.py e posizionalo in questa cartella, a fianco del notebook) dotato di interfaccia a linea di comando (CLI).

Lo scopo dell'eseguibile è spostare un singolo file (che si trova nella cartella files) nella sottocartella di competenza, aggiornando il recap.

L'interfaccia dell'eseguibile ha come unico argomento (obbligatorio) il nome del file da spostare (comprensivo di formato, es: 'trump.jpeg'). Nel caso in cui il file passato come argomento non esista, l'interfaccia deve comunicarlo all'utente.



## Step #3

Una immagine in scala di grigio ha un solo livello di colore, una RGB ne ha 3, una RGBA 4 (l'ultimo è detto canale alpha).

Il modulo Image della libreria PIL permette di caricare un'immagine, che può essere trasformata in un array NumPy attraverso la funzione np.array. A partire da tale array, è possibile capire se l'immagine caricata è in scala di grigio, RGB o RGBA.

Aggiungi al notebook dello Step 1 uno script che iteri sulla sottocartella images e costruisca una tabella riassuntiva come questa (prodotta con la libreria tabulate):

![image](https://github.com/user-attachments/assets/748a293f-ed51-4fb2-b0e1-2f14ad5a1ef3)


Oltre al nome del file, la tabella riporta:

altezza dell'immagine, in pixel
larghezza dell'immagine, in pixel
se l'immagine è in scala di grigio, la colonna grayscale indica la media dei valori dell'unico livello di colore
se l'immagine è a colori, le altre colonne indicano la media dei valori di ogni livello di colore.


Dovrai consegnare:

- un notebook con gli Step 1 e 3; per semplicità puoi chiamarlo come questo
- addfile.py con quanto richiesto dallo Step 2.








tipo e dimensione in byte. Questo è l'output desiderato:
