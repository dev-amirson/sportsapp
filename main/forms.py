from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Team, Player

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': ''}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': ''}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': ''}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': ''}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['city', 'mascot']

class PlayerForm(forms.ModelForm):
    teams = forms.ModelMultipleChoiceField(
        queryset=Team.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'teams']
