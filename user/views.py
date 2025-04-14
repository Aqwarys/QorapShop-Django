from django.shortcuts import render
from django.shortcuts import redirect
from .models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView
from .forms import UserRegistrationForm, UserLoginForm

@login_required(login_url='user:login')
def profile(request, username=None):
    if username is None:
        username = request.user.username
    user = User.objects.get(username=username)
    return render(request, 'user/profile.html', context={'user': user})


class UserCreateView(CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('user:profile')
    template_name = 'user/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        if self.object:
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(self, email=email, password=password)

            if user is not None:
                login(self.request, user=user)

        return response

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.get(email=email)
            if user is not None and user.check_password(password):
                login(request, user)
                return redirect(reverse_lazy('user:profile'))

    form = UserLoginForm()
    return render(request, 'user/login.html', {'form': form})

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('shop:home')