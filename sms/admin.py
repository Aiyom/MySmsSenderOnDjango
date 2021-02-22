from django.contrib import admin
from .models import Students, Kurs, SaveMessage


@admin.register(Students)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'sirname', 'kurs', 'dayOfDate', 'timeOfKurs', 'telParents', 'telMe', 'group')


@admin.register(Kurs)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')


@admin.register(SaveMessage)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'id_name', 'data', 'typeOfMessage')