import names
import random
from random import randint
from django.shortcuts import render
from django.views.generic import DetailView
from . import models
# Create your views here.


def home(request):
    return render(request, 'inicio.html')


def profesiones(request):
    return render(request, 'profesiones.html', {
        'profesiones': models.Profesion.objects.all().order_by('nombre')
    })


class ProfesionDetailView(DetailView):
    template_name = 'detalle_profesion.html'
    model = models.Profesion


def get_phone():
    n = '0000000000'
    while '9' in n[3:6] or n[3:6]=='000' or n[6]==n[7]==n[8]==n[9]:
        n = str(random.randint(10**9, 10**10-1))
    return n[:3] + '-' + n[3:6] + '-' + n[6:]


def create_records(request):
    for i in range(90):
        models.Profesional.objects.create(
            nombre_completo=names.get_full_name(),
            telefono='{}'.format(get_phone()),
            correo='email@prueba.com',
            profesion_id=randint(1, 9)
        )
    return render(request, 'inicio.html')


