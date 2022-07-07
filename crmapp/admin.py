from django.contrib import admin
from . models import Lead, User, Agent
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Lead)
admin.site.register(Agent)
