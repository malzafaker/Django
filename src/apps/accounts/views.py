# -*- coding:utf-8 -*-
from django.shortcuts import redirect, get_object_or_404, render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import auth
from django.contrib.auth import logout as auth_logout
from django.views.generic.edit import FormView, View

from apps.accounts.forms import LoginForm


class LoginView(FormView):
    """ Авторизация """
    form_class = LoginForm
    template_name = 'login.jade'

    def form_valid(self, form):
        user = form.get_user()
        auth.login(self.request, user)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class LogoutFormView(View):
    """ Выход из профиля """
    def get(self, request):
        auth_logout(request)
        return redirect('home')

