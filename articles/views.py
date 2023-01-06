from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article

from django.contrib.auth.decorators import login_required    # its  a decorator.. see other decoratos on google
# just add above definition of functions whose view req. login.. argument is .. where to redirect if ! logged in 

from . import form_for_models # contains form for the MOdel Article within it!

def article_list(request):
    articles = Article.objects.all().order_by('date');
    return render(request, 'articles/article_list.html', { 'articles': articles })

def article_detail(request, slug):
    deets=Article.objects.get(slug=slug)
    return render(request, 'articles/article_detailed.html',{'slug_art':deets})


@login_required(login_url="/accounts/login/")
def create_article(request):
    if(request.method=='POST'):
        #see the form_for_models.py file.. it has  a class Create_article
        form=form_for_models.Create_article(request.POST,request.FILES) # This is validating the data ... ! Noice.      # files when we upload.. req 2 thing.1) enctype in form in html_templ
        # second... they dont come along the request.POST data.. so second argument.. request.FILES
        
        if(form.is_valid()):
            # now we want to add user also... and since we dont just fet it from Front end ,, we have to get it from logged in user.. so we wont just simply 
            # save it .. first add in the returned instance a user...
            instance=form.save(commit=False) #commit = false.. it wont save in db.. it wont commit this record.. but still the .save() returned the obhject
            instance.author=request.user
            #Modified the instnace. Now save
            instance.save()
            return redirect('articles:list' )
    else:
        form=form_for_models.Create_article() # creeated the form.. and stored in variable form 
    return render(request,'create_article.html',{'bjha_hua_form':form})