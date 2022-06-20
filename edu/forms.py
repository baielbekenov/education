from django import forms
from django.contrib.admin import options
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from edu.models import Razdel, User, Task, Homework


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'name', 'first_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),

        }


class HomeworkForm(ModelForm):
    class Meta:
        model = Homework
        fields = ['name', 'description', 'file']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),

        }





class RazdelForm(ModelForm):
    class Meta:
        model = Razdel
        fields = '__all__'


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['razdel_id', 'title', 'file', 'is_to_send']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'details-fieldset-section'}),
            'file': forms.FileInput(attrs={'class': 'details-fieldset-section'}),
        }


class HomeworkSendForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['name', 'description', 'file']
        widgets = {
            'Название': forms.TextInput(attrs={'class': 'details-fieldset-section'}),
            'Описание': forms.Textarea(attrs={'class': 'details-fieldset-section'}),
            'Файл': forms.FileInput(attrs={'class': 'details-fieldset-section'}),
        }



