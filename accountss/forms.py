from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField 
from django.forms.forms import Form
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.contrib.auth import get_user_model, password_validation
from django.forms import widgets
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email
from .models import Profile




# class UserRegistrationForm(UserCreationForm):
#     first_name = forms.CharField(label='Prénom')
#     last_name = forms.CharField(label='Nom')
#     email = forms.EmailField(label='Adresse e-mail')

#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = UserCreationForm.Meta.fields + ('first_name' 'last_name', 'email')

# class CouponForm(forms.Form):
#     code = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Promo code',
#         'aria-label': 'Recipient\'s username',
#         'aria-describedby': 'basic-addon2'
#     }))


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    
    class Meta:
        model = User
        fields = ('username',  'email', 'password1', 'password2', )
        

# for profile update
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar'] 

# class CustomUserCreationForm(UserCreationForm):
#     username = forms.CharField(label='Name', min_length=5, max_length=150, widget=forms.TextInput({'class': 'form-control', "id": "name"}))
#     email = forms.EmailField(label='Email', widget=forms.TextInput({'class': 'form-control', "id": "email"}))
#     password1= forms.CharField(label='Password', widget=forms.PasswordInput({'class': 'form-control', "id": "password"}))
#     password2= forms.CharField(label='Confirm Password', widget=forms.PasswordInput({'class': 'form-control', "id": "password_confirmation"}))


#     def clean_username(self):
#         username = self.cleaned_data.get("username")
#         qs = User.objects.filter(username__iexact=username)
#         # if username in non_allowed_usernames:
#         #     raise forms.ValidationError("This is an invalid username, please pick another.")
#         if qs.exists():
#             raise forms.ValidationError("This is an invalid username, please pick another.")
#         return username
    
#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         qs = User.objects.filter(email__iexact=email)
#         if qs.exists():
#             raise forms.ValidationError("This email is already in use.")
#         return email

# captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

# class PasswordResetForm(Password):

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control bg-dark text-light'}))

    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control bg-dark text-light'}), help_text=password_validation. password_validators_help_text_html())

    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control bg-dark text-light'}))

# class LoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(
#         attrs={'autofocus': True, 'class': 'form-control', "id": "email"}))
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={'autocomplete': 'current-password', 'class': 'form-control', "id": "password"}))


class CustomLoginForm(forms.Form):
    username_or_email = forms.CharField(max_length=256, widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control', "id": "email"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control', "id": "password"}))

    def clean_username_or_email(self):
        username_or_email = self.cleaned_data['username_or_email']
        if "@" in username_or_email:
            validate_email(username_or_email)
            data = {'email': username_or_email}
        else:
            data = {'username': username_or_email}
        try:
            get_user_model().objects.get(**data)
        except get_user_model().DoesNotExist:
            raise ValidationError(
                _('This {} does not exist'.format(list(data.keys())[0])))
        else:
            return username_or_email


# class RegisterForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(RegisterForm, self).__init__(*args, **kwargs)

#         self.fields['username'].widget = widgets.TextInput(
#             attrs={'placeholder': "username", "class": "form-control"})
#         self.fields['email'].widget = widgets.EmailInput(
#             attrs={'placeholder': "email", "class": "form-control"})
#         self.fields['password1'].widget = widgets.PasswordInput(
#             attrs={'placeholder': "password", "class": "form-control"})
#         self.fields['password2'].widget = widgets.PasswordInput(
#             attrs={'placeholder': "repeat password", "class": "form-control"})

#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if get_user_model().objects.filter(email=email).exists():
#             raise ValidationError("This email address is already exists.")
#         return email

#     class Meta:
#         model = get_user_model()
#         fields = ("username", "email")


class ForgetPasswordEmailCodeForm(forms.Form):
    username_or_email = forms.CharField(max_length=256,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control',
                                                   'placeholder': 'Type your username or email'}
                                        )
                                        )

    def clean_username_or_email(self):
        username_or_email = self.cleaned_data['username_or_email']
        data = {'username': username_or_email}

        if '@' in username_or_email:
            validate_email(username_or_email)
            data = {'email': username_or_email}
        try:
            get_user_model().objects.get(**data)
        except get_user_model().DoesNotExist:
            raise ValidationError(
                'There is no account with this {}'.format(list(data.keys())[0]))

        if not get_user_model().objects.get(**data).is_active:
            raise ValidationError(_('This account is not active.'))

        return data


class ChangePasswordForm(forms.Form):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'New password'
            }
        ),
    )
    new_password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm password',
            }
        ),
    )

    def clean_new_password2(self):
        password1 = self.cleaned_data['new_password1']
        password2 = self.cleaned_data['new_password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError(_('Passwords are not match'))
        password_validation.validate_password(password2)
        return password2


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(
        attrs={'autocomplete': 'email', 'class': 'form-control bg-dark text-light'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control bg-dark text-light'}), help_text=password_validation. password_validators_help_text_html())

    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control bg-dark text-light'}))


# class CustomerProfileForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ['name', 'locality', 'city', 'state', 'zipcode']
#         widgets = {'name': forms.TextInput(attrs={'class': 'form-control bg-dark text-light'}), 'locality': forms.TextInput(attrs={'class': 'form-control bg-dark text-light'}), 'city': forms.TextInput( attrs={'class': 'form-control bg-dark text-light'}), 
#         'state': forms.Select(attrs={'class': 'form-control bg-dark text-light'}), 
#         'zipcode': forms.NumberInput(attrs={'class': 'form-control bg-dark text-light'})}

