#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Othello, o Reversi (https://en.wikipedia.org/wiki/Reversi), è un gioco da tavolo
giocato da due giocatori su una scacchiera 8x8. Pur avendo regole
relativamente semplici, Othello è un gioco di notevole profondità strategica.
In questo esercizio bisognerà simulare una versione semplificata di othello,
chiamata Dumbothello, in cui un giocatore cattura le pedine dell'avversario in
prossimità della propria pedina appena giocata.
Ecco le regole di Dumbothello:
- ogni giocatore ha un colore associato: bianco, nero;
- il giocatore con il nero è sempre il primo a giocare;
- a turno, ogni giocatore deve mettere una pedina del suo colore in modo tale
  da catturare una o più pedine avversarie;
- catturare una o più pedine avversarie vuol dire che la pedina giocata dal
  giocatore trasforma nel colore del giocatore tutte le pedine avversarie
  direttamente adiacenti, in una qualunque direzione orizzontale, verticale o diagonale;
- dopo aver giocato la propria pedina, le pedine avversarie catturate cambiano
  tutte colore e diventano dello stesso colore del giocatore che ha appena giocato;
- quando il giocatore di turno non può aggiungere ulteriori pedine in gioco,
  la partita termina. Vince il giocatore che ha più pedine sulla scacchiera
  oppure avviene un pareggio se il numero di pedine dei due giocatori è uguale;
- il giocatore di turno non può aggiungere ulteriori pedine se non ha modo di
  catturare nessuna pedina avversaria con nessuna mossa, oppure non ci sono
  più caselle libere sulla scacchiera.

Si deve scrivere una funzione dumbothello(filename) che legga da un file di testo
indicato dalla stringa filename una configurazione della scacchiera e,
seguendo le regole di Dumbothello, generi ricorsivamente l'albero di gioco completo
delle possibili evoluzioni della partita, in modo tale che ogni foglia dell'albero
sia una configurazione da cui non sia più possibile effettuare alcuna mossa.

La configurazione inziale della scacchiera nel file è rappresentata riga per
riga nel file. Una lettera "B" identifica una pedina del nero, una "W" una
pedina del bianco e il carattere "." una casella vuota. Le lettere sono
separate da uno o più caratteri di spaziatura.

In particolare, la funzione dumbothello restituirà una tripla (a, b, c), in cui:
- a è il numero totale di evoluzioni che terminano con una vittoria del nero;
- b è il numero totale di evoluzioni che terminano con una vittoria del bianco;
- c è il numero totale di evoluzioni che terminano con un pari.

Ad esempio, dato in input un file di testo contenente la scacchiera:
. . W W
. . B B
W W W B
W B B W

La funzione ritornerà la tripla:
(2, 16, 0)

ATTENZIONE: la funzione dumbothello o qualche altra 
funzione usata per la soluzione deve essere ricorsiva.

'''


#white=false
#black=true
#space=None

def replaceDati(lines):#farlo con un map********
  ris=[{"B":True,"W":False,".":None}.get(x) for x in lines]#in test grandi magari frega
  space=[x for x,xval in enumerate(ris) if xval==None]
  return ris,space

def fileReader(filename):
  with open(filename,"r",encoding="utf8") as file:
    board,space=[],[]
    ySpace=0
    for lines in file.read().splitlines():
      row=[]
      row,spaceNew=replaceDati(lines.split())
      if spaceNew:space.extend([[ySpace,x] for x in spaceNew])
      board.append(row)
      ySpace+=1#vedere come evitare un ciclo inutile
  return board,space



def result(board,half):
  b,w=0,0
  for y in board:
    b+=y.count(True)
    w+=y.count(False)
    if b>half or w>half:#un po' statistico ma....
      return 0 if b>w else 1 
  if b==w:return 2
  return 0 if b>w else 1
  
def validMove(space,board,colorVs):
    ris=[]
    for y,x in space:
      passed=False
      for yadd,xadd in ((0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)):
        try:
          if board[y+yadd][x+xadd]==colorVs and y+yadd>=0 and x+xadd>=0 :
              if not passed:
                boardNext=list(map(list.copy,board))
                passed=True                   #cambiare***************************************
                boardNext[y][x]=not colorVs
              boardNext[y+yadd][x+xadd]=not colorVs
        except:continue
      if passed:ris.append((y,x,boardNext))
    return ris

def resultCreate(board,space,color,half):
    validMoves=validMove(space,board,not color)
    ris=[0,0,0]
    if validMoves:
      for y,x,boardNext in validMoves:
        spaceNext=space[:]
        spaceNext.remove([y,x])
        risNew=resultCreate(boardNext,spaceNext,not color,half)
        ris[0]+=risNew[0]   #alto codice
        ris[1]+=risNew[1]
        ris[2]+=risNew[2]
    else: ris[result(board,half)]=+1
    return ris


def dumbothello(filename : str) -> tuple[int,int,int] :
    # il tuo programma va qui  
    board,spacePosition=fileReader(filename)
    half=int((len(board)*len(board[0]))/2)#valore di controllo pregenerato
    return tuple(resultCreate(board,spacePosition,True,half))

if __name__ == "__main__":
    R = dumbothello("boards/01.txt")
    print(R)
