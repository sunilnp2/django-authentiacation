from django.contrib import admin
from .models import *
# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id','name','review','tick']
admin.site.register(Review, ReviewAdmin)