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

