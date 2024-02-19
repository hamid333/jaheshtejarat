from django.shortcuts import render


# Create your views here.

def transportation(request):
    return render(request, 'transportation/transportation.html')


def maritime(request):
    return render(request, 'transportation/maritime.html')

def air(request):
    return render(request, 'transportation/air.html')

def road(request):
    return render(request, 'transportation/road.html')


