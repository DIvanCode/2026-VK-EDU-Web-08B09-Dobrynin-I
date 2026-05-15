from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import transaction

from .models import Profile


class SignupForm(forms.Form):
    login = forms.CharField(
        min_length=3,
        max_length=20,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "reg-login"}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "id": "reg-email"})
    )
    nickname = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "reg-nickname"}),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "id": "reg-password"},
            render_value=True,
        ),
    )
    password2 = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "id": "reg-password-repeat"},
            render_value=True,
        ),
    )
    avatar = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={"class": "form-control", "id": "reg-avatar"}
        ),
    )

    def clean_login(self):
        login = self.cleaned_data["login"]
        if User.objects.filter(username=login).exists():
            raise ValidationError("This login is already registered.")
        return login

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        return email

    def clean_password1(self):
        password = self.cleaned_data["password1"]
        user = User(
            username=self.data.get("login", ""),
            email=self.data.get("email", ""),
            first_name=self.data.get("nickname", ""),
        )
        validate_password(password, user)
        return password

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            self.add_error("password2", "Passwords do not match.")
        return cleaned_data

    @transaction.atomic
    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data["login"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password1"],
            first_name=self.cleaned_data["nickname"],
        )
        Profile.objects.create(user=user, avatar=self.cleaned_data.get("avatar"))
        return user


class LoginForm(forms.Form):
    login = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "id": "login-name"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "id": "login-pass"},
            render_value=True,
        )
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        login = cleaned_data.get("login")
        password = cleaned_data.get("password")

        if login and password:
            self.user = authenticate(
                self.request,
                username=login,
                password=password,
            )
            if self.user is None:
                raise ValidationError("Please enter a correct login and password.")

        return cleaned_data
