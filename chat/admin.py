
# Register your models here.
from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('username', 'content', 'timestamp')
    search_fields = ('username', 'content')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)
