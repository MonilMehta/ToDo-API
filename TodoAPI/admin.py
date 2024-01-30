# TodoAPI/admin.py
from django.contrib import admin
from .models import ToDo, Profile

admin.site.register(ToDo)
admin.site.register(Profile)
