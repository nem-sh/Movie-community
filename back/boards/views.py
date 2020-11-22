from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from .models import Movie,Review,Comment, LikeMovie, Test,Genre
from accounts.serializers import UserSerializer
from .serializers import TestSerializer, LikeMovieSerializer,UserLikeMovieSerializer, MovieSerializer, MovieListSerializer, ReviewSerializer, ReviewListSerializer, CommentSerializer, ReviewDetailSerializer,ReviewDeleteSerializer
from accounts.models import LikeUser, User
import json
import random
# Create your views here.
@api_view(['POST'])
def search(request):
    print(request.data)
    data = request.data['searchValue']
    print(request.data)
    movies = Movie.objects.filter(title__icontains=data)
    movies2 = Movie.objects.filter(original_title__icontains=data)
    reviews = Review.objects.filter(title__icontains=data)
    users = User.objects.filter(username__icontains=data)
    users2 = User.objects.filter(name__icontains=data)
    movie_serial = MovieSerializer(movies,many=True)
    movie_serial2 = MovieSerializer(movies2,many=True)
    review_serial = ReviewSerializer(reviews, many=True)
    user_serial = UserSerializer(users, many=True)
    user_serial2 = UserSerializer(users2, many=True)

    return Response([movie_serial.data+movie_serial2.data,review_serial.data,user_serial.data+user_serial2.data])


@api_view(['POST'])
def user(request):
    userserial = UserSerializer(request.user)

    likemovies = request.user.likemovie_set.filter(score__gte=4)
    likeserial = UserLikeMovieSerializer(likemovies, many=True)
    return Response([userserial.data,likeserial.data])


@api_view(['get'])
def profile(request,user_pk):
    user = get_object_or_404(User, pk=user_pk)
    userserial = UserSerializer(user)


    likemovies = user.likemovie_set.filter(score__gte=4)
    likeserial = UserLikeMovieSerializer(likemovies, many=True)
    return Response([userserial.data,likeserial.data])


@api_view(['GET'])
def movie(request):
    print(request.data)
    genres = Genre.objects.order_by('-pk')
    data = []
    for genre in genres:
        g = {}
        g['name'] = genre.name
        g['movie'] = MovieSerializer(genre.movies,many=True).data
        data.append(g)
    # print(g)
    return Response([data])


@api_view(['GET'])
def reviews(reqeust):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)
    
@api_view(['POST'])
def index(request):
    
    if request.user.is_authenticated:
        likeusers = LikeUser.objects.filter(me=request.user).filter(like__gte=2)
        mylikeusers = []
        for likeuser in likeusers:
            mylikeusers.append(likeuser.you)
        userializer = UserSerializer(mylikeusers,many=True)
        recomend = set()
        for user in mylikeusers:
            likeusersmovies = LikeMovie.objects.filter(user=user).filter(score__gte=4)
            for movie in likeusersmovies:
                recomend.add(movie.movie)
        mymovies = LikeMovie.objects.filter(user=request.user)
        for movie in mymovies:
            recomend.discard(movie.movie)
        recomend = list(recomend)
        reserializer = MovieListSerializer(recomend, many=True)


        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response([random.sample(serializer.data, 20), userializer.data ,reserializer.data])
    
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response([random.sample(serializer.data, 20), [] ,[]])


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_create(request, movie_pk):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(writer=request.user)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_update(request, movie_pk, review_pk):
    
    data = request.data
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.writer:
        review.title = request.data['title']
        
        review.content = request.data['content']
        review.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=403)

@api_view(['POST'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie_serializer = MovieSerializer(movie)
    reviews = movie.review_set.order_by('-pk')
    review_serializer = ReviewListSerializer(reviews, many=True)
    if request.user.is_authenticated:
        if movie.likemovie_set.filter(user=request.user).exists():
            like_movie = movie.likemovie_set.filter(user=request.user)
            like_serializer = LikeMovieSerializer(like_movie, many=True)
            return Response([movie_serializer.data ,review_serializer.data,like_serializer.data])
        else:
            return Response([movie_serializer.data ,review_serializer.data,[{'score': 0}]])
    else:
        return Response([movie_serializer.data ,review_serializer.data,[{'score': 0}]])



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_pk, review_pk):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(writer=request.user)
        return Response(serializer.data)

@api_view(['POST'])
def reivew_detail(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    review_serializer = ReviewSerializer(review)
    
    if request.user == review.writer:
        is_writer =True
    else:
        is_writer = False
    comments = review.comment_set.order_by('-pk')
    comment_serializer = CommentSerializer(comments, many=True)
    return Response([review_serializer.data,comment_serializer.data,{'isWriter': is_writer}])

@api_view(['GET'])
def reivew_detail_comments(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.order_by('-pk')
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.writer:
        review.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=403)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_delete(request, movie_pk, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.writer:
        comment.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=403)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def likelike(request,movie_pk):
    print(request.data)
    score = request.data['score']
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.likemovie_set.filter(user=request.user).exists():
        print('sss')
        like_movie = movie.likemovie_set.filter(user=request.user)
        print(12313)
        if (like_movie[0].score >=3 and score <3) or (like_movie[0].score <3 and score >=3):
            
            like_movie2 = movie.likemovie_set.order_by('-pk')
            for i in range(len(like_movie2)):
                if like_movie2[i].user == request.user: continue
                if (like_movie2[i].score >=3 and score <3) or (like_movie2[i].score <3 and score >=3):
                    likeuser = get_object_or_404(LikeUser, me=request.user, you=like_movie2[i].user)
                    
                    likeuser2 = get_object_or_404(LikeUser, you=request.user, me=like_movie2[i].user)
                    likeuser.like -=2
                    likeuser2.like -=2
                    likeuser.save()
                    likeuser2.save()
                else:
                    likeuser = get_object_or_404(LikeUser, me=request.user, you=like_movie2[i].user)
                    likeuser2 = get_object_or_404(LikeUser, you=request.user, me=like_movie2[i].user)
                    likeuser.like +=2
                    likeuser2.like +=2
                    likeuser.save()
                    likeuser2.save()
        serializer = LikeMovieSerializer(data=request.data, instance=like_movie[0])
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
    else:
        
        print(1)
        like_movie = movie.likemovie_set.order_by('-pk')
        print(like_movie)
        if score >= 3:
            print(3)
            print(1,len(like_movie))
            for i in range(len(like_movie)):
                if like_movie[i].user == request.user: continue
                print(3)
                if like_movie[i].score >=3:
                    
                    if LikeUser.objects.filter(me=request.user).filter(you=like_movie[i].user).exists():
                        likeuser = get_object_or_404(LikeUser, me=request.user, you =like_movie[i].user)
                        likeuser2 = get_object_or_404(LikeUser, you=request.user, me =like_movie[i].user)
                        likeuser2.like +=1
                        likeuser.like +=1
                        likeuser.save()
                        likeuser2.save()
                    else:
                        likeuser = LikeUser(me=request.user, you=like_movie[i].user, like=1)
                        likeuser2 = LikeUser(you=request.user, me=like_movie[i].user, like=1)
                        likeuser.save()
                        likeuser2.save()
                else:
                    if LikeUser.objects.filter(me=request.user).filter(you=like_movie[i].user).exists():
                        likeuser = get_object_or_404(LikeUser, me=request.user, you =like_movie[i].user)
                        likeuser2 = get_object_or_404(LikeUser, you=request.user, me =like_movie[i].user)
                        likeuser2.like -=1
                        likeuser.like -=1
                        likeuser.save()
                        likeuser2.save()
                    else:
                        likeuser = LikeUser(me=request.user, you=like_movie[i].user, like=-1)
                        likeuser2 = LikeUser(you=request.user, me=like_movie[i].user, like=-1)
                        likeuser.save()
                        likeuser2.save()
            print(5)
        else:
            for i in range(len(like_movie)):
                
                if like_movie[i].user == request.user: continue
                if like_movie[i].score >=3:
                    
                    if LikeUser.objects.filter(me=request.user).filter(you=like_movie[i].user).exists():
                        likeuser = get_object_or_404(LikeUser, me=request.user, you =like_movie[i].user)
                        likeuser2 = get_object_or_404(LikeUser, you=request.user, me =like_movie[i].user)
                        likeuser2.like -=1
                        likeuser.like -=1
                        likeuser.save()
                        likeuser2.save()
                    else:
                        likeuser = LikeUser(me=request.user, you=like_movie[i].user, like=-1)
                        likeuser2 = LikeUser(you=request.user, me=like_movie[i].user, like=-1)
                        likeuser.save()
                        likeuser2.save()
                else:
                    if LikeUser.objects.filter(me=request.user).filter(you=like_movie[i].user).exists():
                        likeuser = get_object_or_404(LikeUser, me=request.user, you =like_movie[i].user)
                        likeuser2 = get_object_or_404(LikeUser, you=request.user, me =like_movie[i].user)
                        likeuser2.like +=1
                        likeuser.like +=1
                        likeuser.save()
                        likeuser2.save()
                    else:
                        likeuser = LikeUser(me=request.user, you=like_movie[i].user, like=1)
                        likeuser2 = LikeUser(you=request.user, me=like_movie[i].user, like=1)
                        likeuser.save()
                        likeuser2.save()
                # if like_movie[i].score >=3:
                #     likeuser = LikeUser(me=request.user, you=like_movie[i].user, like=-1)
                #     likeuser.save()
                #     likeuser = LikeUser(you=request.user, me=like_movie[i].user, like=-1)
                #     likeuser.save()
                # else:
                #     likeuser = LikeUser(me=request.user, you=like_movie[i].user, like=1)
                #     likeuser.save()
                #     likeuser = LikeUser(you=request.user, me=like_movie[i].user, like=1)
                #     likeuser.save()
        serializer = LikeMovieSerializer(data=request.data)
        print(1)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            print(request.data)
            return Response(serializer.data)

@api_view(['POST'])
def test(request):
    print('a')
    print(request.data)
    test = Test()
    test.img = request.data['img']
    
    test.name = request.data['name']
    test.save()
    test = Test(id=1)
    print(test.name)
    print(test)
    print(22)

@api_view(['GET'])
def testt(request):
    test = get_object_or_404(Test, pk=11)
    print(11)
    print(test.name)
    serializer = TestSerializer(test)
    return Response(serializer.data)
    

@api_view(['POST'])    
def profile_update(request, user_pk):
    if request.user.pk == user_pk:
        user = get_object_or_404(User,pk=user_pk)
        print(request.data['img'])
        user.img = request.data['img']
        
        user.one_thing = request.data['one_thing']
        user.save()
        return HttpResponse(status =200)
    else:
        return HttpResponse(status =400)