#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib2 import *           # Para hacer wget
from os import system           # Para ejecutar reproductor video

# Cargamos las categorias
Numero=sys.argv[1]
Origen="https://www.facebook.com/search/top/?q="+Numero
print Origen
Puntero=urlopen(Origen)
Contenido=Puntero.read()
Puntero.close()

# Hemos leido la pagina de inicio y ahora buscamos categorias
Contador=1
for l in Contenido.split('\n'):
        # Encontramos la cadena
        #print Contador
        if "<!--" in l:
                s=l.split('<!--')
                f=s[1].split('<div>')
                for j in f:
                        if "32mo" in j:
                                web=j[j.index("href=\"")+6:j.index("data-testid")-2]
                                Nombre=j[j.index("_32mo")+7:j.index("</div>")]
                                print Numero+" - "+Nombre+" - "+web
        Contador+=1
