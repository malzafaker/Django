# -*- coding:utf-8 -*-
# from captcha.fields import CaptchaField

from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import gettext as _

from apps.accounts.utils import get_password_random
from apps.accounts.models import User


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", 'last_name', 'first_name', 'middle_name', 'phone_number',)
        widgets = {
            'last_name': forms.TextInput(attrs={
                'class': 'g-width-90 m-input-cycle m-hidden',
                'name': 'last_name',
                'id': 'last_name',
                'placeholder': _(u"Например: Сергеев"),
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'g-width-90 m-input-cycle m-hidden',
                'name': 'first_name',
                'id': 'first_name',
                'placeholder': _(u'Например: Дмитрий')
            }),
            'middle_name': forms.TextInput(attrs={
                'class': 'g-width-90 m-input-cycle m-hidden',
                'name': 'middle_name',
                'id': 'middle_name',
                'placeholder': _(u'Например: Сергеевич')
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'g-width-90 m-input-cycle inputmaskphone',
                'name': 'phone_number',
                'id': 'phone_number',
                'placeholder': _(u'Например:') + ' +7 937 234 43 45',
                'data-inputmask': "'alias': 'inputmaskphone'"
            }),
            'email': forms.TextInput(attrs={
                'class': 'g-width-90 m-input-cycle',
                'name': 'email',
                'id': 'email',
                'placeholder': _(u'Например:') + ' My_email@mail.ru'
            }),
        }

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        password = get_password_random()
        user.set_password(password)
        user.username = self.cleaned_data["email"]
        user.is_active = True
        user.save()
        return user


class UserCreationFormAnybody(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", 'last_name', 'first_name', 'middle_name', 'phone_number',)
        widgets = {
            'last_name': forms.TextInput(attrs={
                'class': 'g-width-90 m-input-cycle ',
                'name': 'last_name',
                'id': 'last_name',
                'placeholder': _(u"Например: Сергеев"),
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'g-width-90 m-input-cycle',
                'name': 'first_name',
                'id': 'first_name',
                'placeholder': _(u'Например: Дмитрий')
            }),
            'middle_name': forms.TextInput(attrs={
                'class': 'g-width-90 m-input-cycle',
                'name': 'middle_name',
                'id': 'middle_name',
                'placeholder': _(u'Например: Сергеевич')
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'g-width-90 m-input-cycle inputmaskphone',
                'name': 'phone_number',
                'id': 'phone_number',
                'placeholder': _(u'Например:') + ' +7 937 234 43 45',
                'data-inputmask': "'alias': 'inputmaskphone'"
            }),
            'email': forms.TextInput(attrs={
                'class': 'g-width-90 m-input-cycle',
                'name': 'email',
                'id': 'email',
                'placeholder': _(u'Например:') + ' My_email@mail.ru'
            }),

        }

    def save(self, commit=True):
        user = super(UserCreationFormAnybody, self).save(commit=False)
        user.username = self.cleaned_data["email"]
        user.set_password(get_password_random())
        user.is_active = False
        user.save()
        return user


class UserChangeForm(forms.ModelForm):
    def save(self, commit=True):
        user = super(UserChangeForm, self).save(commit=False)
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('email',)


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()

    error_messages = {
        'invalid_login': _("Please enter a correct %(username)s and password. "
                           "Note that both fields may be case-sensitive."),
        'inactive': _("This account is inactive."),
    }

    def get_user(self):
        return self.user_cache

    def clean(self):
        username = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(
                username=username,
                password=password
            )
            if self.user_cache is None or self.user_cache.is_active is False:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login'
                )
        return self.cleaned_data


# class PasswordForm(forms.Form):
#     email = forms.CharField()
#     captcha = CaptchaField()
