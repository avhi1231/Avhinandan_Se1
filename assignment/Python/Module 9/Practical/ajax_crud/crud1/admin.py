from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import Item

@admin.register(Item)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','description')