from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser
#
#
# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('codemeli')}),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('codemeli')}),
#     )
#     list_display = ['codemeli', 'email', 'username', 'is_staff']
