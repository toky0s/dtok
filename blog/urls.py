from django.urls import path
from . import views


app_name='blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<slug:slug>', views.detail , name='detail'),
    path('delete/<int:comment_id>', views.comment_delete, name='delete_comment')
]