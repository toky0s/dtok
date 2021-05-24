from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from blog.models import Tag, BlogArticle
from .forms import RegisterForm
from .models import InformationArticle
from . import views

# Create your views here.

def index(request):
    tags = Tag.objects.all()
    information_articles = InformationArticle.objects.all()
    articles = BlogArticle.objects.all()
    context = {
        'tags': tags,
        'information_articles': information_articles,
        'articles': articles,
    }
    return render(request, 'home/home.html', context)

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home:register_success'))
    return render(request, 'registration/register.html', context={'register_form':form})

def register_success(request):
    return HttpResponse("Đăng ký thành công <a href=\"/\">Về trang chủ</a>")



