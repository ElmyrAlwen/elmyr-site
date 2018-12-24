from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_main/<int:pk>/', views.post_detail, name='post_detail'),
    path('post_main/', views.post_main, name='post_main'),
    path('gallery/', views.gallery, name='gallery'),
    path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
]