from django.contrib import admin
from django.urls import path
from comments import views

urlpatterns = [
    path('post_comment',views.post_comment , name='post_comment'),
    path('',views.home,name='home'),
    path('<str:slug>', views.getpage, name='getpage'),
    path('comment/',views.comment_list),
    path(r'^(?P<id>\d+)/delete/', views.comment_delete, name='delete'),


]
