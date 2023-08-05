from django.contrib import admin

from users.models import User


# admin.site.register(User)

@admin.register(User)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email','last_login', 'is_active')
