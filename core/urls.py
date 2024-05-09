from django.urls import path, include
from.import views
from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path('index', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('accounts/profile/', views.index, name='index'),
    path('accounts/profile/logout', views.logout, name='logout'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('', include(tf_urls)),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),

]

