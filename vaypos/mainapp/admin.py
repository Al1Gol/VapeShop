from django.contrib import admin
from mainapp.models import Products, Category

# Register your models here.
admin.site.register(Products)
admin.site.register(Category)

def str(self):
    return '%s' % (self.name)

Category.__str__ = str

Products.__str__ = str

