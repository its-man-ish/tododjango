from django.contrib import admin
from .models import TodoModel
# Register your models here.
@admin.register(TodoModel)

class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','work','time','email',)