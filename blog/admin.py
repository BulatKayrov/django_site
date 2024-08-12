from django.contrib import admin

from blog.models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'category', 'is_published', 'created_at', 'count_views')
    list_filter = ('category', 'created_at', 'author', 'is_published', 'count_views')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('count_views', 'created_at')
    list_editable = ['is_published']
    fields = (
        ('title', 'slug', 'image'),
        ('author', 'category', 'is_published'),
        ('created_at', 'updated_at'),
        'content', 'count_views'
    )
