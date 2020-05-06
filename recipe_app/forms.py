from django import forms
from recipe_app.models import Author


class AddAuthorForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name'
    }
    ))

    bio = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Short bio...'}
    ))

    class Meta:
        model = Author
        fields = ['name', 'bio']


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
