from django.shortcuts import render

from .models import *


# Create your views here.

def transportation(request):
    about = Transportation_About.objects.order_by('-id').first()
    members = Transportation_Members.objects.filter(status=1)
    certificate = Transportation_Certificate.objects.filter(status=1)
    context = {
        'about': about,
        'members': members,
        'certificate': certificate,
    }
    return render(request, 'transportation/transportation.html', context)


def maritime(request):
    maritime = Transportation_Maritime.objects.order_by('-id').first()
    context = {
        'maritime': maritime
    }
    return render(request, 'transportation/maritime.html', context)


def air(request):
    air = Transportation_Air.objects.order_by('-id').first()
    context = {
        'air': air
    }
    return render(request, 'transportation/air.html', context)


def road(request):
    road = Transportation_Road.objects.order_by('-id').first()
    context = {
        'road': road
    }
    return render(request, 'transportation/road.html', context)
