# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import forms, login ,logout  # .auth means authentication models.. mah nig

# Create your views here.
def signup_view(request):
    if (request.method =='POST'):
        form=forms.UserCreationForm(data=request.POST) #isse jo dataa aaya post request k saath usse form bnega and saved in form
        if (form.is_valid()):
            user=form.save()  # this does 2 things... savesthe form(sign ups the user) and also returns the user(name) ... 
            login(request,user)
            return redirect('articles:list')# so now it signs up and also logs in ... and then rediredct to articles page 
        
    else:  # request is get.. so what u do is .. take the required form and send it in the template 
        form=forms.UserCreationForm()
    return render(request,'signup_page.html',{'form_info':form})  # by default request is get.. 

def login_page(request):
    if(request.method=='POST'): 
        print("ok")
        #agr user hai toh log in else.. dekh le 
        form=forms.AuthenticationForm(data=request.POST) #django forms not only give Forms ka code..  but give the CORRESPONDING validation way also!
        # by validation i dont mean that password>8 char & all... it also means.. wheather user exists in database or not! Thats the magic 
        if(form.is_valid()):
            user=form.get_user()
            login(request,user)# log the user in 
            # if next naamak info aaya hai request k 7.... toh uski value pe redirect 
            if( 'next' in request.POST):
                return redirect(request.POST.get('next'))
            return redirect('articles:list')


    else:
        form=forms.AuthenticationForm()
    return render(request,'login_template.html',{'form':form})

def logout_page(request):
    if(request.method=='POST'):
        logout(request)
        return redirect('articles:list')
