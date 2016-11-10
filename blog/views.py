from django.shortcuts import render
from utesteder import models as uModels
from blog import models as bModels
from .models import Article, ArticleComment
from .forms import CommentForm
from django.contrib.auth.models import User
from django.utils import timezone

def index(request, p):
    e = 2.7182818284
    page = int(p)
    end = page*10
    articles = Article.objects.filter(frontpage=True).order_by('-publishDate')[:4]
    all_articles = Article.objects.order_by("-publishDate")[end-10:end]
    popular_articles = Article.objects.order_by("-publishDate")[:20] #TODO: fiks slik at de sorterer etter mest populære
    scores = []
    auth = None
    if request.user.is_authenticated():
        auth = request.user
    for i, a in enumerate(popular_articles):
        days = (timezone.now().microsecond - a.publishDate.microsecond)
        scores.append((a,a.hit_count*(1/days)))
    scores = sorted(scores, key=lambda tup:tup[1], reverse=True)[:5]
    popular_articles = [i[0] for i in scores]


    article_count = len(Article.objects.all())
    max_page = (article_count // 10)
    if article_count % 10 > 0:
        max_page+=1
    pages = []
    start = 1
    end = max_page+1
    nextpage = 0
    prevpage = 0
    if page < max_page:
        nextpage = page+1
    if page > 1:
        prevpage = page-1
    if page > 4:
        if (page + 3) > max_page:
            if max_page > 6:
                start = max_page-6
        else:
            if max_page > 6:
                start = page-3
                end = page+3
    else:
        if max_page > 6:
            end = 7
    for i in range(start,end):
        pages.append(i)

    return render(request,'blog/home.html', {'articles':articles,'all_articles':all_articles,'popular_articles':popular_articles,'page':page,'pages':pages,
                                             'next_page':nextpage,'prev_page':prevpage,'auth':auth})

def article(request, id):
    article = Article.objects.get(pk=id)
    comments = ArticleComment.objects.filter(article=article)
    popular_articles = Article.objects.order_by("publishDate")[:5] #TODO: fiks slik at de sorterer etter mest populære
    related_articles = article.tags.similar_objects()[:3]
    auth = None
    if request.user.is_authenticated():
        auth = request.user
    if request.method == "GET":
        return render(request,'blog/article.html',{'article':article,'comments':comments, 'form':CommentForm(),
                                                   'popular_articles':popular_articles
                                                   ,'related_articles':related_articles, 'auth':auth})
    elif request.method == "POST":
        return_message = ""
        if request.user.is_authenticated():
            recieved_form = CommentForm(data=request.POST)
            print(recieved_form.data['body'])
            if recieved_form.is_valid():
                object = ArticleComment.objects.create(body=recieved_form.data['body'], user=request.user, article=article)
                object.save()
                return_message = "Kommentaren ble lagt til vellykket"
            else:
                return_message = "Tekstfeltet må fylles ut for å legge igjen en kommentar"
        else:
            return_message = "Du må logge inn for å legge igjen en kommentar"


        return render(request,'blog/article.html',{'article':article,'comments':comments, 'form':CommentForm(),
                                                   'return_message':return_message,'popular_articles':popular_articles
                                                   ,'related_articles':related_articles, 'auth':auth})


def page_count(request,id):
    article = Article.objects.get(pk=id)
    article.hit_count += 1
    article.save()
