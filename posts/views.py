from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from datetime import datetime


# Create your views here.
def index(request):
    article_records = Post.objects.all()
    article_list = list()

    for count, article in enumerate(article_records):
        article_list.append("#{}: {}<br>".format(str(count), str(article)))
        article_list.append(
            "<small>{}</small><br><hr>".format(article.content))
        article_list.append("slug:{}<br><hr>".format(article.slug))

    return HttpResponse(article_list)


def about(request):
    return HttpResponse("hello world")


def index_use_template(requests):
    article_records = Post.objects.all()
    # print(article_records)
    now = datetime.now()
    # return render(requests, "index.html", locals())
    return render(requests, 'pages/home.html', locals())


def showPost(requests, slug):
    article = Post.objects.get(slug=slug)
    return render(requests, 'pages/post.html', locals())


def login(requests):
    return render(requests, 'pages/login.html')
