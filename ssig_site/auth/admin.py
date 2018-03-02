from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    def clean_password(self):
        return self.initial['password']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserChangeForm

    list_display = ('upi', 'email', 'full_name', 'department')
    list_filter = ('is_superuser',)
