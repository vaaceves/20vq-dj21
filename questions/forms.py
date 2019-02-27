from django import forms
from django.contrib.auth.models import User


# CONSTANT
# PARAMETERS
ERROR_MESSAGE_USER = {
    'required': 'Username is required',
    'unique': 'That Username is not available, try another one',
    'invalid': 'The Username format is incorrect, try another one'
}

ERROR_MESSAGE_PASSWORD = {
    'required': 'Password is required',
    'invalid': 'The Password format is incorrect, password must be at leat 8 characters long and contain a number or a symbol'
}

ERROR_MESSAGE_EMAIL = {
    'required': 'Email is required',
    'unique': 'That Email adress is already registered, try another one',
    'invalid': 'The Email format incorrect, try a valid email adress'
}


# FORMS
# LOGIN
class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')


# SIGN UP
class SignUpUserForm(forms.ModelForm):
    username = forms.CharField(max_length=20, error_messages=ERROR_MESSAGE_USER, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(error_messages=ERROR_MESSAGE_EMAIL, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=20, error_messages=ERROR_MESSAGE_PASSWORD, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).count():
            raise forms.ValidationError('That email is already registered in other account')
        return email