from django.contrib import admin
from .models import Movie, Review, LikeMovie
# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(LikeMovie)