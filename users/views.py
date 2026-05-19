from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.views import generic
"""
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})"""

class RegisterView(generic.CreateView):
    template_name = 'users/register.html'
    form_class = UserCreationForm
    success_url = '/login/'
"""
def auth_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/user_list/')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

"""
class AuthLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return '/user_list/'
    
"""def auth_logout_view(request):
    logout(request)
    return redirect('/login/')"""
class AuthLogoutView(LogoutView):
    next_page = '/login/'
"""
def user_list_view(request):
    if request.method == 'GET':
        user_list = User.objects.all()
    return render(request, 'users/user_list.html', {'user_list': user_list})


"""
class UserListView(generic.ListView):
    template_name = 'users/user_list.html'
    context_object_name = 'user_list'
    model = User