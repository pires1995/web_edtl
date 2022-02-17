from django import forms
from appointment.models import Appointment, ContactMunicipality
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class DateInput(forms.DateInput):
    input_type = 'date'

class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateField(widget=DateInput(), required=True)
    appointment_time = forms.TimeField(required=True)
    email = forms.EmailField(required=True, widget=forms.EmailInput())
    mobile = forms.IntegerField(required=True, max_value=8)
    class Meta: 
        model = Appointment
        fields = ['first_name', 'last_name', 'email', 'mobile', 'appointment_date', 'appointment_time','subject']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-4 mb-0'),
                Column('last_name', css_class='form-group col-md-4 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),	
                Column('mobile', css_class='form-group col-md-4 mb-0'),	
                css_class='form-row'
            ),
            Row(
                Column('appointment_date', css_class='form-group col-md-6 mb-0'),
                Column('appointment_time', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('subject', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary" type="submit"><i class="bi bi-lock text-white"></i> Rai</button> """)
        )

class ContactForm(forms.ModelForm):
    class Meta: 
        model = ContactMunicipality
        fields = ['name', 'phone_number', 'position', 'municipality']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('phone_number', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('position', css_class='form-group col-md-6 mb-0'),
                Column('municipality', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary" type="submit"><i class="bi bi-lock text-white"></i> Rai</button> """)
        )

