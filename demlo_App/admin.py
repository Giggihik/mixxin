from django.contrib import admin
from .models import UserWithPhone, Service, Request

admin.site.register(UserWithPhone)
admin.site.register(Service)
admin.site.register(Request)