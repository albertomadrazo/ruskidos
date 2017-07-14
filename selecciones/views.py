from django.shortcuts import render
from django.http import HttpResponse

from .models import Confederacion, Seleccion, Jugador

def index(request):
	confederacion = Confederacion.objects.get(pk=1)
	jugadores = Jugador.objects.all()
	context = {
		'confederacion':confederacion,
		'jugadores':jugadores,
	}
	# return HttpResponse('Holy fuck!')
	return render(request, 'selecciones/index.html', context)

def getSeleccion(request, seleccion):
	seleccion = Seleccion.objects.get()

def jugador(request, numero):
	jugador = Jugador.objects.get(numero=int(numero))
	jugador = {
			'nombre':jugador.nombre,
			'numero':jugador.numero,
	}
	print(jugador['nombre'])
	return render(request, 'selecciones/jugador.html', jugador)