from os import times
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField, RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingField
from users.models import DtokUser
import datetime

# Create your models here.
class InformationArticle(models.Model):
    author = models.ForeignKey(DtokUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    create_date = models.DateTimeField(default=timezone.now)
    modify_date = models.DateTimeField(default=timezone.now)
    view = models.IntegerField(default=0)
    content = RichTextUploadingField(blank=False)
    url_slug = models.SlugField(max_length=500, default=None, null=True, blank=False)
    

    def __str__(self):
        return self.title