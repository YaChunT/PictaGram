from. import views
from django.contrib import admin
from django.urls import path
from django.urls import include
from two_factor.urls import urlpatterns as tf_urls
from . import views


# urlpatterns = [
#     path('', include(tf_urls)),
#     path('', views.IndexView.as_view(), name='index'),
#     path('settings', views.IndexView.as_view(), name='settings'),
#     path('upload', views.IndexView.as_view(), name='upload'),
#     path('follow', views.IndexView.as_view(), name='follow'),
#     path('search', views.IndexView.as_view(), name='search'),
#     path('profile/<str:pk>', views.IndexView.as_view(), name='profile'),
#     path('like-post', views.IndexView.as_view(), name='like-post'),
#     path('signup', views.signup, name='signup'),
#     path('signin', views.signin, name='signin'),
#     path('logout', views.IndexView.as_view(), name='logout'),
#     path('settings', views.IndexView.as_view(), name='settings'),
# ]


urlpatterns = [
    path('', include(tf_urls)),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('settings', views.settings, name='settings'),
]
