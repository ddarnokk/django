from django.shortcuts import render


def sell(request):
    return render(request, "oferta.html", {})