from django.contrib import admin
from users.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    ordering = ('username',)
    list_filter = ('email',)
    search_fields = ('email',)

admin.site.register(User, UserAdmin)
