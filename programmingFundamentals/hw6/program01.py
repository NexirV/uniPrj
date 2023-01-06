#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Siete stati appena ingaggiati in una software house di videogiochi e
dovete renderizzare su immagine il giochino dello snake salvando
l'immagine finale del percorso dello snake e restituendo la lunghezza
dello snake.
Si implementi la funzione generate_snake che prende in ingresso un
percorso di un file immagine, che e' l'immagine di partenza
"start_img" che puo' contenere pixel di background neri, pixel di
ostacolo per lo snake di colore rosso e infine del cibo di colore
arancione. Lo snake deve essere disegnato di verde. Inoltre bisogna 
disegnare in grigio la scia che lo snake lascia sul proprio
cammino. La funzione inoltre prende in ingresso una posizione iniziale
dello snake, "position" come una lista di due interi X e Y. I comandi
del giocatore su come muovere lo snake nel videogioco sono disponibili
in una stringa "commands".  La funzione deve salvare l'immagine finale
del cammino dello snake al percorso "out_img", che e' passato come
ultimo argomento di ingresso alla funzione. Inoltre la funzione deve
restituire la lunghezza dello snake al termine del gioco.

Ciascun comando in "commands" corrisponde ad un segno cardinale ed e
seguito da uno spazio. I segni cardinali possibli sono:

| NW | N | NE |
| W  |   | E  |
| SW | S | SE |

che corrispondono a movimenti dello snake di un pixel come:

| alto-sinistra  | alto  | alto-destra  |
| sinistra       |       | destra       |
| basso-sinistra | basso | basso-destra |

Lo snake si muove in base ai comandi passati e nel caso in cui
mangia del cibo si allunga di un pixel.

Lo snake puo' passare da parte a parte dell'immagine sia in
orizzontale che in verticale. Il gioco termina quando sono finiti i
comandi oppure lo snake muore. Lo snake muore quando:
- colpisce un ostacolo
- colpisce se stesso quindi non puo' passare sopra se stesso
- si incrocia in diagonale in qualsiasi modo. Ad esempio, un percorso
  1->2->3-4 come quello sotto a sinistra non e' lecito mentre quello a
  destra sotto va bene.

  NOT OK - diagonal cross        OK - not a diagonal cross
       | 4 | 2 |                    | 1 | 2 |
       | 1 | 3 |                    | 4 | 3 |

Ad esempio considerando il caso di test data/input_00.json
lo snake parte da "position": [12, 13] e riceve i comandi
 "commands": "S W S W W W S W W N N W N N N N N W N" 
genera l'immagine in visibile in data/expected_end_00.png
e restituisce 5 in quanto lo snake e' lungo 5 pixels alla
fine del gioco.

NOTA: analizzate le immagini per avere i valori esatti dei colore da usare.

NOTA: non importate o usate altre librerie
'''



#arancione 255,128,0:cibo
#verde 0,255,0:snake
#rosso 255, 0, 0:ostacoli
#nero 0; 0; 0;sfodo "tua madre"
#grigio 128,128,128:scia

#vedere se e' meglio passare solo le parti della lista da controllare
#vedere se e' meglio tradurre la lista prima di farci elaborazioni spora e poi ritradurla

#utile usare le classi?

import images

def generate_snake(start_img: str, position: list[int, int],
                   commands: str, out_img: str) -> int:
    # Scrivi qui il tuo codice
    listapixel=images.load(start_img)#vedere se si puo' evitare images prima
    s=Snake(position,listapixel)
    for comando in commands.split():
      if s.comando(comando)==False:break


    images.save(s.getMap(),out_img)
    return s.getLunghezza()
    pass

class Snake:      #singleton ma evito perche' non necessario e penso meno efficente considerando che non supportato in modo diretto

  _cibo=(255,128,0)
  _ostacolo=(255,0,0)
  _serpente=(0,255,0)
  _sfondo=(0,0,0)
  _scia=(128,128,128)
  _dizionarioComandi={"N":[-1,0],"S":[1,0],"W":[0,-1],"E":[0,1],"NW":[-1,-1],"NE":[-1,1],"SW":[1,-1],"SE":[1,1]}

  def __init__(self,posizione,listapixel):
    self._corpoSer=[tuple(posizione)]         #snake body (for snake track)
    self._x=posizione[0]                      #snake x
    self._y=posizione[1]                      #snake y
    self._map=listapixel                      #all pixel
    self._height=len(listapixel)              #pixel h img
    self._width=len(listapixel[0])            #pixel w img
    pass
  
  def getLunghezza(self):return len(self._corpoSer)
  def getMap(self):return self._map

  def comando(self,direzione):
    y,x=self._dizionarioComandi[direzione]

    x=(x+self._x)%self._width
    y=(y+self._y)%self._height

    if len(direzione)>1:#==2
      if self._map[y][self._x]==self._serpente and self._map[self._y][x]==self._serpente:return False #vedere se si puo scivere tipo and di entrambi uguale al serpente

    if self._map[y][x]==self._ostacolo or self._map[y][x]==self._serpente:return False

    self._x=x
    self._y=y
    self._corpoSer.append((x,y))

    if self._map[y][x]==self._cibo:
      self._map[y][x]=self._serpente
      return  
      
    self._map[y][x]=self._serpente
    self._map[self._corpoSer[0][1]][self._corpoSer[0][0]]=self._scia
    self._corpoSer.pop(0)
    pass
    
      

