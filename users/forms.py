from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import PasswordResetForm
from .models import *
from django.contrib.auth.forms import UserChangeForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        help_text='A valid email address, please.', required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        # Add CSS classes to form fields
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Username'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Last Name'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Email Address'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Confirm Password'})

        # Set labels to empty strings
        self.fields['username'].label = ''
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['email'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class StaffForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.')
    access_level = forms.ChoiceField(
        choices=CustomUser.ACCESS_LEVEL_CHOICES, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', 'access_level']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'form-control', 'placeholder': field.label})

        self.fields['username'].label = ''
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['email'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        self.fields['access_level'].label = ''

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.access_level = self.cleaned_data['access_level']

        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email*")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))


class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']


class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)


class UserUpdateForm(UserChangeForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, required=False)
    is_active = forms.BooleanField(required=False)
    access_level = forms.ChoiceField(
        choices=get_user_model().ACCESS_LEVEL_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'password',
                  'confirm_password', 'access_level', 'is_active']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
