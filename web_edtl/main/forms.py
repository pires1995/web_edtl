from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import Group
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML, Field
from main.models import User
from appointment.models import Appointment, Suggestion
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from crispy_bootstrap5.bootstrap5 import FloatingField
from finance.models import Bill
from news.models import NewsUser

class DateInput(forms.DateInput):
    input_type = 'date'

class DateTimesInput(forms.TimeField):
    input_type = 'time'

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
        self.fields['groups'].queryset = Group.objects.all().exclude(name='client')
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

class AppointmentForm(forms.ModelForm):
    first_name = forms.CharField(label="Fullname", required=True)
    appointment_date = forms.DateField(widget=DateInput(), required=True)
    appointment_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    class Meta:
        model = Appointment
        fields = ['first_name', 'appointment_to', 'email', 'mobile', 'appointment_date', 'appointment_time', 'subject']

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class="form-group col-md-4 mb-0"),
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('mobile', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('appointment_date', css_class="form-group col-md-4 mb-0"),
                Column('appointment_time', css_class='form-group col-md-4 mb-0'),
                Column('appointment_to', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('subject', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary text-white" name="appointment_form" type="submit">Submit</button> """)
        )

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['fullname','email', 'mobile', 'text']

    def __init__(self, *args, **kwargs):
        super(SuggestionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('fullname', css_class="form-group col-md-4 mb-0"),
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('mobile', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('text', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary text-white" name="suggestion_form" type="submit">Submit</button> """)
        )


class FMSLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class':'form-group col-md-12 py-2',
                'placeholder': 'Enter your Email'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-group col-md-12 py-2',
                'placeholder': 'Enter your Password'
            }
        )
    )



class BillForm(forms.ModelForm):
    payment_date = forms.DateField(widget=DateInput(), required=True)   
    class Meta:
        model = Bill
        fields = ['bill_number','payment_date','file']
        labels = {
            'file': 'Image',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('bill_number', css_class='form-group col-md-4 mb-0'),
                Column('payment_date', css_class='form-group col-md-4 mb-0'),
                Column('file', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary" type="submit"> Chave <i class="fa fa-save"></i></button> """)
        )

class USMForm(forms.ModelForm):
    class Meta:
        model = NewsUser
        fields = ['email']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary" type="submit"> Submit <i class="fa fa-save"></i></button> """)
        )