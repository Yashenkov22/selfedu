from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-input'}),
            'content' : forms.Textarea(attrs={'cols' : 60, 'rows' : 10}),
            'slug' : forms.TextInput(attrs={'placeholder' : 'Имя должно быть уникальным', 'class' : 'form-input'}),
        }

class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class' : 'form-input'}))
    email = forms.EmailField(label='E-mail',widget=forms.EmailInput(attrs={'class' : 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class' : 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class' : 'form-input'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class' : 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class' : 'form-input'}))

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols' : 60, 'rows' : 10}))
    captcha = CaptchaField()