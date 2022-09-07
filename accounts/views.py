from pathlib import Path
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView
from django.shortcuts import render
from accounts.forms import RegistrationForm, LoginForm
from accounts.models import UserLocation
from hackathon.utils import DataMixin
from operator import attrgetter
from itertools import chain


class RegisterUser(DataMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts-locations')

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(current_page='accounts-register')

        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):

        user = form.save()
        login(self.request, user)

        return redirect('accounts-locations')


class LoginUser(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(current_page='accounts-login')

        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):

        return reverse_lazy('accounts-locations')


def logout_user(request):
    logout(request)
    return redirect('accounts-login')


class ProfilePage(DataMixin, TemplateView, LoginRequiredMixin):
    template_name = 'accounts/accounts.html'

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy(self.get_login_url()))

        locations = UserLocation.objects.filter(user=request.user).order_by('-date')

        context = self.get_user_context(
            current_page='accounts-locations',
            user=request.user,
            locations=locations
        )

        return render(request, self.template_name, context=context)


class LocationPage(DataMixin, TemplateView, LoginRequiredMixin):
    template_name = 'accounts/location.html'

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy(self.get_login_url()))

        # locations = UserLocation.objects.filter(user=request.user).order_by('-date')

        context = self.get_user_context(
            user=request.user,
            # locations=locations
        )

        return render(request, self.template_name, context=context)
