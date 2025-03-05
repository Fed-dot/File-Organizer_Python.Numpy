# selezione delle librerie necessarie
import sys, os, shutil, csv, argparse

# impostazione della directory in cui sono posizionati i file 
os.chdir(os.path.join(os.path.dirname(sys.argv[0]),'files'))

# lo script crea le cartelle necessarie per trasferire i dati, se non sono già presenti
os.makedirs(os.path.join(os.getcwd(),'Audio'),mode = 0o777, exist_ok = True)   
os.makedirs(os.path.join(os.getcwd(),'Docs'),mode = 0o777, exist_ok = True)
os.makedirs(os.path.join(os.getcwd(),'Images'),mode = 0o777, exist_ok = True)

# funzione per visualizzare i path originari dei file ed il path di destinazione rispetto alla tipologia
def locate(x):
        return os.path.join(os.getcwd(),x)
    
# struttura dati "formats" divisa per tipologia, estensione e sottocarella di destinazione dei file per tipo
formats = {'Image':[('jpg','jpeg','png'),locate('Images')],
               'Audio':[('mp3'),locate('Audio')],
               'Doc': [('odt','txt'),locate('Docs')]}

# lista per la scrematura dei file presenti in os.listdir rispetto alla tipologia elencata nella struttura dati "formats"
files_list=[]
for ext in formats.values():
    for file in sorted(os.listdir()):
        if file.endswith(ext[0]):
            files_list.append(file)

# creazione di una funzione che sposti i file in base all'argomento specificato dall'utente, creando un file .csv di recap

def file_sort(file):
    
# creazione del file "recap.csv"    
    recap_exists = os.path.isfile("recap.csv")
    with open("recap.csv", mode="a", newline='') as csvfile:
        fieldnames = ["name","type","size(B)"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

# la funzione riscrive le intestazioni delle colonne del file "recap.csv" solo se non già esistenti

        if not recap_exists:
            writer.writeheader() 

# iterazione tra i file presenti nella cartella "files"
        for x in sorted(os.listdir()):
# iterazione nella struttura dati "formats" per l'associazione del file scelto con la propria tipologia e cartella di destinazione
            for name,ext in formats.items():
# clausola if per evitare la selezione delle sotto cartelle create nella cartella "files" ('Images','Audio','Docs')
                if file.endswith(ext[0]):
# trasferimento dei file nella cartella di destinazione rispetto alla tipologia e 
                    shutil.move(locate(file),os.path.join(ext[1],file))
# i file trasferiti sono segnati contemporaneamente nel file "recap.csv" creato precedentemente
                    size = str(os.path.getsize(os.path.join(ext[1],file)))
                    writer.writerow({"name":file.split('.')[0],"type": name,"size(B)": size})
# l'utente viene avvisato sul file trasferito e sulla cartella di destinazione
                    return "il file {} è stato spostato nella directory {}".format(file,ext[1])
                

# la libreria 'argparse' descrive le funzioni fornite dallo script e lo rende esguibile da terminale secondo l'argomento predisposto "file"
# la funzione try-except riporta un messaggio specifico all'utente nel caso fosse scelto un file non presente nella cartella di origine
try:   
    parser = argparse.ArgumentParser(description="Eseguibile per spostare singoli file di tipologia differente dalla cartella di provenienza, alla sotto cartella della tipologia corrispondente",exit_on_error=False)
    
# l'argomento fa riferimento alla lista dinamica "files_list", aggiornata in base alle estensioni dei file desiderati segnati in "formats" 
    parser.add_argument("file", help = "inserire nome completo del file da ordinare", choices = files_list)
    args = parser.parse_args()
except argparse.ArgumentError:
    print('il file scelto non è presente nella cartella di origine, selezionare un file dalla seguente lista: \n{}'.format(files_list))

# in questo caso la funzione try-except evita il NameError conseguente alla scelta di un argomento non valido
try:
    print(file_sort(args.file))
except NameError:
    pass
