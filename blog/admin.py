from django.contrib import admin
from .models import BlogArticle, Comment, Tag


# Register your models here.
admin.site.register([Tag, BlogArticle, Comment])