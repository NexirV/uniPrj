#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Obiettivo dello homework è leggere alcune stringhe contenute in una serie di
file e generare una nuova stringa a partire da tutte le stringhe lette.
Le stringhe da leggere sono contenute in diversi file, collegati fra loro a
formare una catena chiusa. Infatti, la prima stringa di ogni file è il nome di
un altro file che appartiene alla catena: partendo da un qualsiasi file e
seguendo la catena, si ritorna sempre nel file di partenza.

Esempio: il contenuto di "A.txt" inizia con "B.txt", il file "B.txt", inizia
con "C.txt" e il file "C.txt" inizia con "A.txt", formando la catena
"A.txt"-"B.txt"-"C.txt".

Oltre alla stringa con il nome del file successivo, ogni file contiene anche
altre stringhe separate da spazi, tabulazioni o caratteri di a capo. La
funzione deve leggere tutte le stringhe presenti nei file della catena e
costruire la stringa che si ottiene concatenando i caratteri con la più alta
frequenza in ogni posizione. Ovvero, nella stringa da costruire, alla
posizione p ci sarà il carattere che ha frequenza massima nella posizione p di
ogni stringa letta dai file. Nel caso in cui ci fossero più caratteri con
la stessa frequenza, si consideri l'ordine alfabetico.
La stringa da costruire ha lunghezza pari alla
lunghezza massima delle stringhe lette dai file.

Quindi, si deve scrivere una funzione che prende in ingresso una stringa A 
che rappresenta il nome di un file e restituisce una stringa.
La funzione deve costruire la stringa secondo le indicazioni illustrate sopra
e ritornare le stringa così costruita.

Esempio: se il contenuto dei tre file A.txt, B.txt e C.txt nella directory
test01 è il seguente

test01/A.txt          test01/B.txt         test01/C.txt                                                                 
-------------------------------------------------------------------------------
test01/B.txt          test01/C.txt         test01/A.txt
house                 home                 kite                                                                       
garden                park                 hello                                                                       
kitchen               affair               portrait                                                                     
balloon                                    angel                                                                                                                                               
                                           surfing                                                               

la funzione most_frequent_chars("test01/A.txt") dovrà restituire la stringa
"hareennt".
'''

#NOTA: non considero le frequenze perche' le considero come una limitazione dei test.

def creazioneLista(fileScor):
    primoFile=fileScor
    strFile=list()
    while True: #do while
        with open(fileScor,"r",encoding="utf8") as file:
            file=file.read().split()
            fileScor=file[0]#non metto l'assegnazione dopo perche' meno efficente dato che in questo caso faccio solo 1 assegnazione inutile mentre nell altro vado a leggere 2 volte usando gli indici per ogni file
            strFile.extend(file[1:])
            if primoFile==fileScor:
                break
    return tuple(strFile)

def freqMassima(dizionario):
    #vedere se fare altre assegnazioni prima
    if len(dizionario)<30: #algoritmo piu' rapido in casi piccoli
        return freqListaPiccola(dizionario)
    else: #algoritmo piu' rapido in casi grandi
        max_value = max(dizionario.values())
        return min((k for k,v in dizionario.items() if v == max_value))

def freqListaPiccola(dizionarioPiccolo):#la freq piu' grande ha piu' probabilita' di trovarsi all'inizio quindi evito il sorted
    valMax=0
    for key,val in dizionarioPiccolo.items():
        if val>valMax:
            valMax=val
            listRis=[key]
        elif val==valMax:
            listRis.extend(key)
    return min(listRis)


def calcoloDizionario(lunghezza):
    return [{} for c in range(lunghezza)]

def most_frequent_chars(filename: str) -> str:
    # SCRIVI QUI LA TUA SOLUZIONE
    strFile=creazioneLista(filename)
    if strFile==():return str()    #caso di file con solo collegamento al file sucessivo e poi 
    listaLettere=calcoloDizionario(len(max(strFile, key=len)))
    for string in strFile:
        for s,dict in zip(string,listaLettere):
            try: dict[s]+=1 
            except KeyError:dict[s]=1  #"convenzionale"
    return str().join(map(freqMassima,listaLettere))                                                                 
    pass

if __name__ == '__main__':
    print(most_frequent_chars("ProvaMia/wewe.txt"))
    pass




