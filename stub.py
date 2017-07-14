import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fut.settings")
django.setup()


from selecciones.models import Confederacion, Seleccion, Jugador

c = Confederacion()
c.nombre = 'CONCACAF'

c.save()

s = Seleccion()
s.nombre = 'Mexico'
s.confederacion = c
s.save()

j = Jugador()
j.nombre = 'Guillermo Ochoa'
j.numero = 1
j.seleccion = s
j.save()

j = Jugador()
j.nombre = 'Javier Hernandez'
j.numero = 14
j.seleccion = s
j.save()