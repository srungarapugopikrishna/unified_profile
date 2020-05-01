from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class InputUserProfileForm(forms.Form):
    # name = forms.CharField(label='name')
    # username = forms.CharField(label='username')
    email = forms.EmailField(label='E-Mail')
    facebook = forms.URLField(label='facebook', required=False)
    instagram = forms.URLField(label='Instagram', required=False)
    twitter = forms.URLField(label='Twitter', required=False)
    github = forms.URLField(label='Github', required=False)
    stackoverflow = forms.URLField(label='Stackoverflow', required=False)
    resume = forms.URLField(label='Resume', required=False)
    hackerrank = forms.URLField(label='HackerRank', required=False)
    hackerearth = forms.URLField(label='HackerEarth', required=False)
    others = forms.URLField(label='other links. Seperated by comma(,)', required=False)


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )