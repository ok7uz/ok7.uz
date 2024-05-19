from django.contrib import admin

from project.models import *


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    fields = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'started_date', 'finished_date')
    filter_horizontal = ('tags',)
    # fields = ('name',)