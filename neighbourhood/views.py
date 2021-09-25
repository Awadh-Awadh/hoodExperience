from django.shortcuts import render,redirect
from .forms import CustormUserCreationForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustormUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustormUserCreationForm()
    context = {
      'form': form
    }
    return render(request, 'neighbourhood/register.html', context)
