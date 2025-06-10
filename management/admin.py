from django.contrib import admin

from .models import Emp

# Register your models here.


class EmpAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'phone','working')  
    list_editable = ('phone','working')
    search_fields=('name',)

admin.site.register(Emp, EmpAdmin)
