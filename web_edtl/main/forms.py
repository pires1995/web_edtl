from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import Group
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML, Field
from main.models import User


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user', 'placeholder': 'Enter Your Email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': 'Enter Your Password',
        }
    ))


class CustomUserForm(forms.ModelForm):
    # first_name = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'form-control col-md-3 mb-0'}))
    # gpname = Group.objects.all()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'groups', 'mobile']

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        self.fields['groups'].queryset = Group.objects.all()
        self.fields['groups'].required = True
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class="form-group col-md-4 mb-0"),
                Column('last_name', css_class='form-group col-md-4 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('mobile', css_class='form-group col-md-4 mb-0'),
                Column('groups', css_class='form-group col-md-8 mb-0',
                       required=True),
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary text-white" type="submit"><i class="bi bi-lock text-white"></i> Save</button> """)
        )
