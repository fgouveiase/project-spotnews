from django.contrib import admin

# Register your models here.

from .models import Users, News, Categories

admin.site.register(Users)
admin.site.register(News)
admin.site.register(Categories)
