from django.shortcuts import render
from .models import Sell

def sell(request):
    sells = Sell.objects.all()

    return render(request, "oferta.html", {"sells" : sells})