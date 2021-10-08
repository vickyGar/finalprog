from django.shortcuts import render, redirect
from .models import tabla

def index(request):
    if request.method == "POST":
        print(request.POST.get('nombre') + ' ' + request.POST.get('apellido') + ' ' + request.POST.get('computo'))
        _empleado = tabla(nombre=request.POST.get('nombre'),
                          apellido=request.POST.get('apellido'),
                          computo=request.POST.get('computo'))

        _empleado.save()
        return redirect('web:table')

    return render(request, 'index.html')

def table(request):
    allEmpleado = tabla.objects.all()
    print(allEmpleado)
    return render(request, 'table.html', {'table':allEmpleado})

def updateEmpleado(request, pk_tabla):
    _empleado = tabla.objects.get(pk_tabla=pk_tabla)
    if request.method == "POST":
        _empleado.nombre = request.POST.get('nombre')
        _empleado.apellido = request.POST.get('apellido')
        _empleado.computo = request.POST.get('computo')
        _empleado.save()
        return redirect('web:table')
    return render(request, 'index.html', {'empleado':_empleado})

def deleteEmpleado(request, pk_tabla):
    _empleado = tabla.objects.get(pk_tabla=pk_tabla)
    _empleado.delete()
    return redirect('web:table')