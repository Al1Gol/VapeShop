"""vaypos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path

import mainapp.views as mainapp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.main, name = 'main' ),
    path('esigs/', mainapp.esigs, name = 'esigs' ),
    path('address/', mainapp.address, name = 'address' ),
    path('aikos/', mainapp.aikos, name = 'aikos' ),
    path('liquid/', mainapp.liquid, name = 'liquid' ),
    path('pods/', mainapp.pods, name = 'pods' ),
    path('address/', mainapp.address, name = 'address' ),
    path('contacts/', mainapp.contacts, name = 'contacts' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)