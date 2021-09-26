from django.shortcuts import render,redirect
from .forms import CustormUserCreationForm
from django.core.mail import send_mail
from django.conf import settings




# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustormUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            subject = 'Welcome to Hood Experince'
            message = f"Hello {username} Thank you for registering with us"
            email_from = settings.EMAIL_HOST_USERNAME
            recipient_list = [email]
            send_mail( subject,message,email_from,recipient_list)
            return redirect('login')
    else:
        form = CustormUserCreationForm()
    context = {
      'form': form
    }
    return render(request, 'hood/register.html', context)



def hero(request):
    return render(request, 'hood/hero.html')