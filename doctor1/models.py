from django.db import models

# Create your models here.
class Doctor(models.Model):
   idDoctor=models.AutoField(primary_key=True)
   nombre=models.CharField(max_length=100)
   especialidad=models.CharField(max_length=100)
   telefono=models.CharField(max_length=100)
   correoElectronico=models.CharField(max_length=100)
   fechaRegistro = models.DateField()

   def __str__(self):
     fila="nombre:"+ self.nombre +"-" +"especialidad:"+ self.especialidad
     return fila