from django.contrib import admin
from .models import Favorite, User, Album, Artist, Favorite

admin.site.register(User)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Favorite)