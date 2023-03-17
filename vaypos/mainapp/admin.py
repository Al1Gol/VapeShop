from django.contrib import admin
from mainapp.models import ProductItem, Menu

# Register your models here.
admin.site.register(ProductItem)
admin.site.register(Menu)

def str(self):
    return '%s' % (self.name)

Menu.__str__ = str

ProductItem.__str__ = str

