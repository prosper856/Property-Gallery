from django.contrib import admin
from .models import Agent, Property , User

@admin.register(Agent)
class Agent(admin.ModelAdmin):
    list_display = ('name', 'bio', "contact")
    search_fields = ('name', "contact")

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("name", "owner","description","location","price","available","created_at", )
    list_filter = ("name","owner")
    search_fields = ("name","owner")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'address')
    search_fields = ('first_name', 'last_name', 'email')