from django.contrib import admin
from .models import Task
# Register your models here.
@admin.register(Task)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','title','description')

