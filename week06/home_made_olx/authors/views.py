from django.shortcuts import render
from django.contrib.auth.models import User

from .forms import RegisterModelForm

# Create your views here.

# Make it with CBV !!!
def register_view(request):
    form = RegisterModelForm()
    if request.method == 'POST':
        form = RegisterModelForm(data=request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(username=form.cleaned_data.get('username'),
                            					email=form.cleaned_data.get('email'),
                            					password=form.cleaned_data.get('password'))
                return redirect(reverse('author:login'))
            except Exception:
                form.add_error(field='', error='User exists!')
    return render(request, 'registration/register.html', locals())
