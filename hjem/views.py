from django.shortcuts import render, render_to_response
from django.template import loader, context
from django.http import HttpResponse
from django.template.context import RequestContext
from utesteder import models as uModels
from blog.models import Article
# Create your views here.
def index(request):
    articles = Article.objects.filter(frontpage=True).order_by('-publishDate')[:4]
    utesteder = uModels.Utested.objects.order_by('hScore')[:6]
    auth = None
    if request.user.is_authenticated():
        auth = request.user

    return render(request,"hjem/body.html",{'articles':articles,'utesteder':utesteder,'auth':auth})