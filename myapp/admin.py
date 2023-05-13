from django.contrib import admin
from .models import Osoba, Majitel, Najemnik, Nemovitost, Najem

# Register your models here.
admin.site.register(Osoba)
admin.site.register(Majitel)
admin.site.register(Najemnik)
admin.site.register(Nemovitost)
admin.site.register(Najem)
