from logging import LoggerAdapter
from django.shortcuts import render,redirect
from .forms import CustormUserCreationForm,EditProfile
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile ,Neighbourhood, Posts, Business




# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustormUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            subject = "welcome to Awardds"             
            message = f"Hello {username}, thank you for registering to Awardds"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from,recipient_list)
            return redirect('login')
    else:
        form = CustormUserCreationForm()
    context = {
      'form': form
    }
    return render(request, 'hood/register.html', context)



def hero(request):
    return render(request, 'hood/hero.html')

def home(request):
    hood = Neighbourhood.objects.get(admin = request.user)
    print(hood)
    posts = Posts.objects.all()
    context = {
        'posts':posts,
        'hood':hood
    }
    return render(request ,'hood/hoodView.html',context)

def profile(request):
    loggedin_user = request.user
    profile = Profile.objects.get(user=loggedin_user)
    count = Posts.objects.filter(posted_by = loggedin_user).count()   
    posts = Posts.objects.filter( posted_by=loggedin_user).all()
    
    if request.method == 'POST':
        form = EditProfile(request.POST,request.FILES, instance = request.user.profile)
        if form.is_valid():
           obj = form.save(commit = False)
           obj.user = loggedin_user
           form.save()
           return redirect('profile')
    else:
        form = EditProfile()
    context = {
        'profile':profile,
        'count':count,
        'form':form,
        'posts':posts
    }
    return render(request, 'hood/profile.html', context)


def bist(request):
    posts = Posts.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'hood/business.html',context)