from django.contrib import admin
from .models import DemoForm

@admin.register(DemoForm)
class DemoFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')

# Register your models here.
