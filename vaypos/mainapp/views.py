from django.conf import settings
from django.shortcuts import render
from mainapp.models import Menu


# Create your views here.
title = 'Vaypos'
media_url = settings.MEDIA_URL
images = ''

def main(request):
    title = 'Главная'
    el = Menu.objects.all().order_by('priority')
    content = {
        'title': title,
        'media': media_url,
        'elements': el
    }
    print(type(settings.MEDIA_URL), settings.MEDIA_URL)
    return render(request, "mainapp/index.html", content)

def address(request):
    title = 'Адрес'
    content = {
        'title': title,
        'media': media_url + images
    }
    return render(request, "mainapp/address.html", content)

def aikos(request):
    title = 'Айкос'
    content = {
        'title': title,
        'media': media_url + images
    }
    return render(request, "mainapp/aikos.html", content)

def contacts(request):
    title = 'Контакты'
    content = {
        'title': title,
        'media': media_url + images
    }
    return render(request, "mainapp/contacts.html", content)

def esigs(request):
    title = 'Электронные сигареты'
    content = {
        'title': title,
        'media': media_url + images
    }
    return render(request, "mainapp/esigs.html", content)

def liquid(request):
    title = 'Жидкости'
    content = {
        'title': title,
        'media': media_url + images
    }
    return render(request, "mainapp/liquid.html", content)

def pods(request):
    title = 'Поды'
    content = {
        'title': title,
        'media': media_url + images
    }
    return render(request, "mainapp/pods.html", content)