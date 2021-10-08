from django.db import models

# Create your models here.
class tabla(models.Model):
    pk_tabla = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=20, null=False, blank=False)
    apellido = models.CharField(max_length=20, null=False, blank=False)
    computo = models.CharField(max_length=20, null=True, blank=True)
