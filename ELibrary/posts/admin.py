from django.contrib import admin
from posts.models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...

class PostAdmin(admin.ModelAdmin):
    ordering = ('title',)
    list_filter = ('pub_datetime',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)