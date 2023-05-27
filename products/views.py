from django.http import HttpResponse
from .models import Products
from django.shortcuts import render


def index(request):
    product = Products.objects.all()
    return render(request, 'index.html', {'product': product})


def new(request):
    return HttpResponse('New Products')


