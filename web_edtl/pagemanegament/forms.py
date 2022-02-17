from django import forms
from pagemanegament.models import PageManegament
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PageManegamentForm(forms.ModelForm):
    
    description_tet = forms.CharField(required=False,label="Deskrisaun (Tetum)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    description_por = forms.CharField(required=False,label="Deskrisaun (Portugues)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    description_eng = forms.CharField(required=False,label="Deskrisaun (Ingles)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    class Meta: 
        model = PageManegament
        fields = ['name', 'description_tet', 'description_por','description_eng']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-12 mb-0'),	
                css_class='form-row'
            ),
            Row(
                Column('description_tet', css_class='form-group col-md-4 mb-0'),
                Column('description_por', css_class='form-group col-md-4 mb-0'),
                Column('description_eng', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary" type="submit"><i class="bi bi-lock text-white"></i> Rai</button> """)
        )
        