from django.contrib import admin
from .models import User, Album, Artist

admin.site.register(User)
admin.site.register(Album)
admin.site.register(Artist)