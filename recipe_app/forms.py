from django import forms
from recipe_app.models import Author


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
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
