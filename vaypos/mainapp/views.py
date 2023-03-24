from django.conf import settings
from django.shortcuts import render
from mainapp.models import Menu


# Create your views here.
title = 'Vaypos'
media_url = settings.MEDIA_URL
images = ''
el = Menu.objects.all().order_by('priority')

def main(request):
    title = 'Главная'
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
        'media': media_url + images,
        'elements': el
    }
    return render(request, "mainapp/address.html", content)

def contacts(request):
    title = 'Контакты'
    content = {
        'title': title,
        'media': media_url + images,
        'elements': el
    }
    return render(request, "mainapp/contacts.html", content)

def menu(request, url):
    content = {
        'title': title,
        'media': media_url + images,
        'elements': el
    }
    return render(request, "mainapp/products.html", content)