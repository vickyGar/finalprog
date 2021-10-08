from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('table/', table, name='table'),
    path('updateEmpleado/<int:pk_tabla>', updateEmpleado, name="updateEmpleado"),
    path('deleteEmpleado/<int:pk_tabla>', deleteEmpleado, name="deleteEmpleado"),

]