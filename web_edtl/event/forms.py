from django import forms
from event.models import Event
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class DateInput(forms.DateInput):
    input_type = 'date'

class EventForm(forms.ModelForm):
    name_tet = forms.CharField(label="Naran Eventu (Tetum)", required=True)
    name_por = forms.CharField(label="Naran Eventu (Portugues)", required=False)
    name_eng = forms.CharField(label="Naran Eventu (Ingles)", required=True)
    overview_tet = forms.CharField(required=False,label="Deskrisaun Eventu (Tetum)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    overview_por = forms.CharField(required=False,label="Deskrisaun Eventu (Portugues)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    overview_eng = forms.CharField(required=False,label="Deskrisaun Eventu (Ingles)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    start_date = forms.DateField(widget=DateInput(), required=False)
    end_date = forms.DateField(widget=DateInput(), required=False)
    class Meta: 
        model = Event
        fields = ['name_tet', 'name_por', 'name_eng', 'overview_tet', 'overview_por','overview_eng','image', 'start_date', 'end_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name_tet', css_class='form-group col-md-4 mb-0'),
                Column('name_por', css_class='form-group col-md-4 mb-0'),
                Column('name_eng', css_class='form-group col-md-4 mb-0'),	
                css_class='form-row'
            ),
            Row(
                Column('overview_tet', css_class='form-group col-md-4 mb-0'),
                Column('overview_por', css_class='form-group col-md-4 mb-0'),
                Column('overview_eng', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('start_date', css_class='form-group col-md-4 mb-0'),
                Column('end_date', css_class='form-group col-md-4 mb-0'),
                Column('image', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary" type="submit"><i class="bi bi-lock text-white"></i> Rai</button> """)
        )
        