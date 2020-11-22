from rest_framework import serializers
from accounts.serializers import UserSerializer

from .models import Movie, Review, Comment, LikeMovie, Test, Genre

class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')

class MovieSerializer(serializers.ModelSerializer):
    
    genres = GenreSerializer(required=False,many=True)
    class Meta:
        model = Movie
        fields = ('id','title','original_title','release_date','popularity','vote_count','vote_average','adult','overview','original_language','poster_path','genres')

    #     title = models.CharField(max_length=100)
    # original_title = models.CharField(max_length=100)
    # release_date = models.DateField()
    # popularity = models.FloatField()
    # vote_count = models.IntegerField()
    # vote_average = models.FloatField()
    # adult = models.BooleanField()
    # overview = models.TextField()
    # original_language = models.CharField(max_length=100)
    # poster_path = models.CharField(max_length=100)
    # backdrop_path = models.CharField(max_length=100)
    # genres = models.ManyToManyField(Genre, related_name='movies')
    # video 

class ReviewListSerializer(serializers.ModelSerializer):
    writer = UserSerializer(required=False)
    movie = MovieSerializer(required=False)


    class Meta:
        model = Review
        fields = ('id', 'title', 'writer', 'content','movie')

class ReviewSerializer(serializers.ModelSerializer):
    writer = UserSerializer(required=False)
    class Meta:
        model = Review
        fields = '__all__'
        # read_only_fields = ('id', 'writer')

class ReviewDetailSerializer(serializers.ModelSerializer):
    writer = UserSerializer(required=False)
    
    movie = MovieSerializer(required=False)

    class Meta:
        model = Review
        fields = '__all__'
        # read_only_fields = ('id', 'writer')

class CommentSerializer(serializers.ModelSerializer):
    writer = UserSerializer(required=False)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id', 'writer')


class ReviewDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'writer')



class LikeMovieSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = LikeMovie
        fields = '__all__'
        
        read_only_fields = ('id', 'user')


class UserLikeMovieSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(required=False)
    class Meta:
        model = LikeMovie
        fields = ('movie','score')
        

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Test
        fields = '__all__'