from django.contrib import admin
from testapp.models import Movie

class MovieAdmin(admin.ModelAdmin):  # ModelAdmin ==> is a parent class, & MovieAdmin ===> is a child class
    list_display = ['moviename', 'rating']
    search_fields = ['hero', 'heroin']

# Register your models here.
admin.site.register(Movie, MovieAdmin)
