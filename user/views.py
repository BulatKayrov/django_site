from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from blog.blog_mixins import TitleMixin
from blog.models import Post
from .forms import UserLoginForm, UserRegisterForm

User = get_user_model()


class ProfileView(TitleMixin, DetailView):
    template_name = 'user/profile.html'
    context_object_name = 'user'
    pk_url_kwarg = 'user_id'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author=self.object)
        return context


class UserLoginView(TitleMixin, LoginView):
    title = 'Авторизация'
    form_class = UserLoginForm
    template_name = 'user/login.html'


class UserRegisterView(TitleMixin, CreateView):
    title = 'Регистрация'
    form_class = UserRegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('user:login')


def logout(request):
    auth.logout(request)
    return redirect(reverse_lazy('blog:index'))

# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return redirect(reverse_lazy('index:index'))
#     else:
#         form = UserLoginForm()
#     context = {
#         'form': form
#     }
#     return render(request, template_name='user/login.html', context=context)
#
#
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth.login(request, user)
#             return redirect(reverse_lazy('index:index'))
#     else:
#         form = UserRegisterForm()
#     context = {
#         'form': form
#     }
#     return render(request, template_name='user/register.html', context=context)
