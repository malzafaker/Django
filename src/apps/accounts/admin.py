# -*- coding: utf-8 -*-
from django.contrib import admin

from apps.accounts.models import User
from apps.accounts.forms import UserChangeForm, UserCreationForm


class UserAdmin(admin.ModelAdmin):
    model = User
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username', 'last_name', 'first_name',)
    list_filter = ('is_superuser', 'is_staff', 'is_active')
    # readonly_fields = ('password',)
    search_fields = ('last_name', 'first_name', 'middle_name', 'username')
    save_on_top = True
    # list_editable = ('',)
    filter_horizontal = ('groups', 'user_permissions',)
    # fieldsets = (
    #     (None, {'fields': ('username', )}),
    #     ('Персональная информация', {'fields': ('email', 'last_name', 'first_name', 'middle_name', 'date_of_birth',
    #                                             'phone_number', 'subdivision')}),
    #     ('Права доступа', {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions', )}),
    #     ('Важные даты', {'fields': ('last_login',)}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'last_name', 'first_name', 'middle_name', 'subdivision', 'phone_number')}
    #      ),
    # )

    # actions = ('test',)

    # def test(self, request, queryset):
    #     self.message_user(request, _('%s ') % repeat_count)
    # added_access_oop.short_description = _('')
