from logging import LoggerAdapter
from django.shortcuts import render,redirect
from .forms import CustormUserCreationForm
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
    return render(request ,'hood/hoodView.html')

def profile(request):
    loggedin_user = request.user
    print(loggedin_user)
    profile = Profile.objects.get(user=loggedin_user)
    count = Posts.objects.filter(posted_by = loggedin_user).count()
   
    # posts = Posts.objects.filter( posted_by=profile).all()
    context = {
        'profile':profile,
        'count':count
    }
    return render(request, 'hood/profile.html', context)