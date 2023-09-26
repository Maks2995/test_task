from django.contrib import admin

from .models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'name', 'desc', 'status', 'date_create', 'date_update', 'link',)
    list_filter = ('author', 'name')


# Register your models here.
