from django.contrib import admin
from .models import User,Student

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_dispaly=('id','name','email','password')

@admin.register(Student)
class MyModelAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('admin/css/custom.css',)
        }
        js = ('admin/js/custom.js',)
class UserAdmin(admin.ModelAdmin):
    list_dispaly=('id','name','email','age','grade')

admin.site.site_header = "My Custom Admin"
admin.site.site_title = "My Admin Portal"
admin.site.index_title = "Welcome to My Admin Dashboard"


