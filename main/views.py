from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from . models import (Album, Author,About, Fact, Skill,
                    Testimonials,Summary,Experience,
                    Education,Service, Category , Contact)
from .forms import ContactForm    
# from django.core.mail import send_mail  
from django.core.mail import EmailMultiAlternatives,EmailMessage              
from django.conf import settings


def home(request):
    authors = Author.objects.all()
    title = 'Home'
    context = {
        'authors':authors,
        'title':title
    }
    return render(request,'index.html',context)
    

def about(request):
    abouts = About.objects.all()
    skills = Skill.objects.all()
    facts = Fact.objects.all()
    title = 'About'
    testimonials = Testimonials.objects.all()
    context = {
        'abouts':abouts,
        'skills':skills,
        'facts':facts,
        'testimonials':testimonials,
        'title':title
    }
    return render(request,'about.html',context)

def contact(request):
    msg = ''
    title = 'Contact'
    forms = ContactForm()
    context = {
        'forms':forms,
        'title':title
    }    
    if request.method == 'POST':
        from_mail = request.POST['contact_email']
        subject = request.POST['contact_subject']
        message = request.POST['contact_message']

        EmailMessage(
            subject,
            message,
            # settings.EMAIL_HOST_USER,
            to=['er.bikhyat@gmail.com','mesooneet@gmail.com'],
            # fail_silently=False
        ).send()  
        msg='message has been sent'  
        context = {
        'forms':forms,
        'msg':msg,
        'title':title
         }    
        return render(request,'contact.html',context)

    return render(request,'contact.html',context)

def portfolio(request):
    title = 'Portfolio'
    cat = request.GET.get('category')
    
    if cat == None:
        albums = Album.objects.all()
    else :
        albums = Album.objects.filter(category__category_name=cat)

    categories = Category.objects.all()
    context = {
        'categories': categories,
        'albums': albums,
        'cat':cat,
        'title':title
    }    
    return render(request,'portfolio.html',context)

def resume(request):
    summaries = Summary.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    title = 'Resume'
    context = {
        'summaries':summaries,
        'educations':educations,
        'experiences':experiences,
        'title':title
    }    
    return render(request,'resume.html',context)

def services(request):
    services = Service.objects.all()
    title = 'Services'
    context = {
        'services':services,
        'title':title
    }
    return render(request,'services.html',context)

 
