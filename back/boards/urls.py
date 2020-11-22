from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [

    path('', views.index, name='index'),
    
    path('user/', views.user, ),
    path('profile/<int:user_pk>/', views.profile, ),
    path('profile_update/<int:user_pk>/', views.profile_update, ),
    path('reviews/', views.reviews, ),
    path('movie_genre/', views.movie, ),
    path('search/', views.search,),
    
    path('<int:movie_pk>/', views.movie_detail, name='detail'),
    path('<int:movie_pk>/review_create/', views.review_create, ),
    path('<int:movie_pk>/likelike/', views.likelike),
    path('<int:movie_pk>/<int:review_pk>/review_detail/', views.reivew_detail),
    
    path('<int:movie_pk>/<int:review_pk>/review_update/', views.review_update),
    path('<int:movie_pk>/<int:review_pk>/comment_create/', views.comment_create),
    
    path('<int:movie_pk>/<int:review_pk>/review_delete/', views.review_delete),
    path('<int:movie_pk>/<int:review_pk>/<int:comment_pk>/comment_delete/', views.comment_delete),
    path('<int:movie_pk>/<int:review_pk>/reivew_detail_comments/', views.reivew_detail_comments),

    path('test/', views.test),
    path('testt/', views.testt),

    
]
