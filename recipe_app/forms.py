from django import forms
from recipe_app.models import Author
from django.contrib.auth.models import User


class AddAuthorForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control my-1',
        'placeholder': 'Name'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control my-1',
        'placeholder': 'Username'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control my-1',
        'placeholder': 'Password'
    }))

    bio = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control my-1',
        'placeholder': 'Short bio...'}
    ))


class AddRecipeForm(forms.Form):
    # def __init__() created with the help of Stack Overflow question
    # https://stackoverflow.com/questions/3532316/django-forms-request-user
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AddRecipeForm, self).__init__(*args, **kwargs)
        if user.is_staff:
            self.fields['author'].queryset = Author.objects.all()
        else:
            self.fields['author'].queryset = Author.objects.filter(user=user)

    title = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'w-50'
    }))
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter description here...'
        }))
    time_required = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={
            'placeholder': 'Ex: One hour'
        }))
    instructions = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Enter Instructions here...'
    }))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Username',
                                   'class': 'form-control'
                               }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control',
    }))
