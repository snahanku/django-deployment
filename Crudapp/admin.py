from django.contrib import admin
#to register  your models here 
# Register your models here.

from  .models import User
class UserAdmin(admin. ModelAdmin):
    list_display=('id' ,'name' , 'email' ,'password')
    