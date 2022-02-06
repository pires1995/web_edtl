from django import forms
from procurament.models import Tender, Guidelines
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class DateInput(forms.DateInput):
    input_type = 'date'

class TenderForm(forms.ModelForm):
    title_tet = forms.CharField(label="Titulu Tender (Tetum)", required=True)
    title_por = forms.CharField(label="Titulu Tender (Portugues)", required=False)
    title_eng = forms.CharField(label="Titulu Tender (Ingles)", required=True)
    description_tet = forms.CharField(required=False,label="Deskrisaun Tender (Tetum)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    description_por = forms.CharField(required=False,label="Deskrisaun Tender (Portugues)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    description_eng = forms.CharField(required=False,label="Deskrisaun Tender (Ingles)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    start_period = forms.DateField(widget=DateInput(), required=False)
    end_period = forms.DateField(widget=DateInput(), required=False)
    class Meta: 
        model = Tender
        fields = ['title_tet', 'title_por', 'title_eng', 'description_tet',\
             'description_por','description_eng', 'start_period', 'end_period', 'file', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('title_tet', css_class='form-group col-md-4 mb-0'),
                Column('title_por', css_class='form-group col-md-4 mb-0'),
                Column('title_eng', css_class='form-group col-md-4 mb-0'),	
                css_class='form-row'
            ),
            Row(
                Column('description_tet', css_class='form-group col-md-4 mb-0'),
                Column('description_por', css_class='form-group col-md-4 mb-0'),
                Column('description_eng', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('start_period', css_class='form-group col-md-6 mb-0'),
                Column('end_period', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('image', css_class='form-group col-md-6 mb-0'),
                Column('file', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary" type="submit"><i class="bi bi-lock text-white"></i> Rai</button> """)
        )

class GuidelinesForm(forms.ModelForm):
    title_tet = forms.CharField(label="Titulu Guidelines (Tetum)", required=True)
    title_por = forms.CharField(label="Titulu Guidelines (Portugues)", required=False)
    title_eng = forms.CharField(label="Titulu Guidelines (Ingles)", required=True)
    description_tet = forms.CharField(required=False,label="Deskrisaun Guidelines (Tetum)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    description_por = forms.CharField(required=False,label="Deskrisaun Guidelines (Portugues)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    description_eng = forms.CharField(required=False,label="Deskrisaun Guidelines (Ingles)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    class Meta: 
        model = Guidelines
        fields = ['title_tet', 'title_por', 'title_eng', 'description_tet',\
             'description_por','description_eng', 'file', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('title_tet', css_class='form-group col-md-4 mb-0'),
                Column('title_por', css_class='form-group col-md-4 mb-0'),
                Column('title_eng', css_class='form-group col-md-4 mb-0'),	
                css_class='form-row'
            ),
            Row(
                Column('description_tet', css_class='form-group col-md-4 mb-0'),
                Column('description_por', css_class='form-group col-md-4 mb-0'),
                Column('description_eng', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('image', css_class='form-group col-md-6 mb-0'),
                Column('file', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary" type="submit"><i class="bi bi-lock text-white"></i> Rai</button> """)
        )