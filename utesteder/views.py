from django.shortcuts import render, render_to_response
from . import models, forms
from django.utils.timezone import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.core.exceptions import ValidationError
from Studenten.settings import LOGIN_URL
from django.http import JsonResponse
# Create your views here.
def index(request):
    byer = models.By.objects.all()
    by = models.By.objects.get(name="Trondheim") #TODO: hardkodet!!1
    #utesteder = by.utested_set.all()
    utesteder = models.Utested.objects.all()
    topScore = 0
    utested = utesteder[0]
    auth = None
    if request.user.is_authenticated():
        auth = request.user
    for u in utesteder:
        if u.hScore > topScore:
            topScore = u.hScore
            utested = u

    apning = utested.apningstider.split(" ")
    priser = utested.olpriser.split(",")
    anmeldelser = utested.anmeldelse_set.all()



    return render(request, 'utesteder/sidebar.html', {'utesteder': utesteder, 'topUtested': utested,
                                                      'byer' : byer,'apningstider':apning,
                                                     'priser':priser, 'anmeldelser':anmeldelser, 'auth':auth})

def utested(request, id, review_amount=5):
    sted = models.Utested.objects.get(pk=id)
    byer = models.By.objects.all()
    by = models.By.objects.get(pk=sted.by_id)
    utesteder = by.utested_set.all()
    apning = sted.apningstider.split(" ")
    priser = sted.olpriser.split(",")
    form = forms.ReviewForm()
    anmeldelser = sted.anmeldelse_set.all().order_by("-review_rating")[:int(review_amount)]
    auth = None
    if request.user.is_authenticated():
        auth = request.user
    if request.method == 'POST':
        received_form = forms.ReviewForm(request.POST) #TODO: sjekk user id!!

        try:
            if not request.user.is_authenticated():
                return HttpResponseRedirect(LOGIN_URL+'?next='+request.path)

            if received_form.is_valid() and received_form.data['hScore'] is not 0:
                object = models.Anmeldelse.objects.create(hScore=received_form.data['hScore'],
                                                 aScore=received_form.data['aScore'],
                                                 pScore=received_form.data['pScore'],
                                                 dScore=received_form.data['dScore'],
                                                 comment=received_form.data['comment'],
                                                 author=request.user.first_name+" "+request.user.last_name,
                                                 utested=sted,
                                                 date=datetime.now()
                                                )
                object.save()
                return render(request, 'utesteder/utested.html',
                              {'utested': sted, 'utesteder': utesteder, 'byer': byer, 'current_by': by,',apningstider': apning,
                               'priser': priser, 'form': form, 'success_message':'Anmeldelsen er registrert!',
                               'anmeldelser':anmeldelser, 'auth':auth})
            else:
                raise ValidationError('Anmeldelsen må inneholde en overall-score')
        except ValidationError as v:
            return render(request, 'utesteder/utested.html',
                          {'utested': sted, 'utesteder': utesteder, 'byer': byer, 'current_by': by,'apningstider': apning,
                           'priser': priser, 'form': form, 'error_message':v.__str__(),'anmeldelser':anmeldelser, 'auth':auth})

    else:
        return render(request,'utesteder/utested.html', {'utested':sted,'utesteder': utesteder,'byer':byer, 'current_by': by,
                                                         'apningstider':apning, 'priser':priser, 'form':form,'anmeldelser':anmeldelser,
                                                         'auth':auth, 'request':request})

def upvote(request, id):
    if request.user.is_authenticated():
        review = models.Anmeldelse.objects.get(pk=id)
        userRating = models.Rating.objects.filter(user_id=request.user.pk).filter(review_id=id)
        print("User",request.user.username,"Review",id,"object",userRating)
        if userRating:
            userRating = userRating[0]
            if userRating.rated == 0:
                userRating.rated = 1
                review.review_rating = review.review_rating + 1
                print("Finnes - raiting satt til 1")
            elif userRating.rated < 0:
                userRating.rated = 0
                review.review_rating = review.review_rating + 1
                print("Finnes - raiting satt til 0 - upvote")
            else:
                return None
            userRating.save()
            review.save()
        else:
            try:
                userRating = models.Rating.objects.create(user=request.user, review=review,rated=1)
                review.review_rating = review.review_rating + 1
                review.save()
                userRating.save()
                print("Finnes ikke - raiting satt til 1")
            except Exception as e:
                print(e)
        return JsonResponse({'new_rating': review.review_rating})

def downvote(request, id):
    if request.user.is_authenticated():
        review = models.Anmeldelse.objects.get(pk=id)
        userRating = models.Rating.objects.filter(user=request.user.pk).filter(review=review.pk)
        if userRating:
            userRating = userRating[0]
            if userRating.rated == 0:
                userRating.rated = -1
                review.review_rating = review.review_rating - 1
                print("Finnes - raiting satt til -1")
            elif userRating.rated > 0:
                userRating.rated = 0
                review.review_rating = review.review_rating - 1
                print("Finnes - raiting satt til 0")
            else:
                return None
            userRating.save()
            review.save()
        else:
            try:
                userRating = models.Rating.objects.create(user=request.user, review=review,rated=-1)
                review.review_rating -= 1
                review.save()
                userRating.save()
                print("Finnes ikke - raiting satt til 1")
            except Exception as e:
                print(e)
        return JsonResponse({'new_rating': review.review_rating})