from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, HttpResponseRedirect

from .forms import CommentForm
from .models import BlogArticle, Comment, Tag

def index(request):
    return HttpResponse("This is blog")

def detail(request, slug):
    tags = Tag.objects.all()
    article = get_object_or_404(BlogArticle, url_slug=slug)

    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, author=request.user, article=article)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponseRedirect(request.path)

    context = {
        'tags': tags,
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'blog/detail.html', context)

@login_required
def delete_comment(request, comment_id):
    pass
