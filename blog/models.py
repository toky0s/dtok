from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.template.defaultfilters import default, slugify
from unidecode import unidecode
from django.utils import timezone
from users.models import DtokUser
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import time

# Create your models here.


class Tag(models.Model):

    author = models.ForeignKey(DtokUser, on_delete=CASCADE)
    display_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    description = RichTextField()
    create_date = models.DateTimeField(default=timezone.now)
    url_slug = models.SlugField(max_length=100, default='url-slug')

    def save(self, *args, **kwargs):
        self.url_slug = slugify(unidecode(self.display_name))
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.full_name


class BlogArticle(models.Model):

    author = models.ForeignKey(DtokUser, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    create_date = models.DateTimeField(default=timezone.now)
    modify_date = models.DateTimeField(default=timezone.now)
    content = RichTextUploadingField()
    view = models.IntegerField(default=0, editable=False)
    url_slug = models.SlugField(max_length=500, default='slug')

    def save(self, *args, **kwargs):
        self.url_slug = slugify(unidecode(str(time.time()) + self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_all_comment(self):
        return self.comments.all()



class Comment(models.Model):

    author = models.ForeignKey(DtokUser, on_delete=CASCADE)
    article = models.ForeignKey(BlogArticle, on_delete=CASCADE, related_name='comments')
    create_date = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=5000)

    def __str__(self):
        return self.article.title