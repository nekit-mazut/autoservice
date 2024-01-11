from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *

from .forms import ClientRegister, AuthenticationForm1, UserProfileForm
from .utils import DataMixin


def base(request):
    return render(request, "main/main.html")


def Service(request):
    return render(request, "main/choosing_a_service.html")


def ds(request):
    return render(request, "main/personal_account.html")


class Base(DataMixin, TemplateView):
    template_name = "main/main.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная")
        return dict(list(context.items()) + list(c_def.items()))


def authorization(request):
    return render(request, 'main/entrans.html')


class Account(LoginRequiredMixin, DataMixin, CreateView):
    template_name = "main/personal_account.html"
    login_url = "/admin/"
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Личный Кабинет")
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = ClientRegister
    template_name = "main/registration.html"
    success_url = reverse_lazy("account")

    def form_valid(self, form):
        response = super().form_valid(form)
        # Выполняем вход в систему после успешной регистрации
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(self.request, user)
        return response

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


class Login(DataMixin, LoginView):
    form_class = AuthenticationForm1
    template_name = 'main/entrans.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))


def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('account')  # или любой другой URL для перенаправления
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'main/personal_account.html', {'form': form})
