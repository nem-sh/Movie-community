from django.contrib import admin
from .models import User, LikeUser
# Register your models here.
admin.site.register(User)
admin.site.register(LikeUser)