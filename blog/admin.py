from django.contrib import admin

from .models import *

@admin.register(Compose)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status')
    list_filter = ('author', 'status')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Feedback)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'pk')