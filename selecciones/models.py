from django.db import models

class Confederacion(models.Model):
	nombre = models.CharField(max_length=200)
	region = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre


class Seleccion(models.Model):
	nombre = models.CharField(max_length=200)
	confederacion = models.ForeignKey(Confederacion, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre


class Jugador(models.Model):
	nombre = models.CharField(max_length=100)
	numero = models.IntegerField()
	seleccion = models.ForeignKey(Seleccion, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre