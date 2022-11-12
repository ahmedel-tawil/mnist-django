from django.contrib import admin
from .models import *
# Register your models here.


class digitsAdmin(admin.ModelAdmin):
    list_display = ('image', 'result', 'created_at')
admin.site.register(Digits, digitsAdmin)
