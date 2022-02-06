from django import forms
from departments.models import Department, Division
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class DepartmentForm(forms.ModelForm):
    name_tet = forms.CharField(label="Naran Departamento (Tetum)", required=True)
    name_por = forms.CharField(label="Naran Departamento (Portugues)", required=False)
    name_eng = forms.CharField(label="Naran Departamento (Ingles)", required=True)
    overview_tet = forms.CharField(required=False,label="Overview Departamento (Tetum)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    overview_por = forms.CharField(required=False,label="Overview Departamento (Portugues)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    overview_eng = forms.CharField(required=False,label="Overview Departamento (Ingles)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    class Meta: 
        model = Department
        fields = ['name_tet', 'name_por', 'name_eng', 'overview_tet', 'overview_por','overview_eng','image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name_tet', css_class='form-group col-md-3 mb-0'),
                Column('name_por', css_class='form-group col-md-3 mb-0'),
                Column('name_eng', css_class='form-group col-md-3 mb-0'),	
                Column('image', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('overview_tet', css_class='form-group col-md-4 mb-0'),
                Column('overview_por', css_class='form-group col-md-4 mb-0'),
                Column('overview_eng', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary" type="submit"><i class="bi bi-lock text-white"></i> Rai</button> """)
        )

class DivisionForm(forms.ModelForm):
    name_tet = forms.CharField(label="Naran Divisaun (Tetum)", required=True)
    name_por = forms.CharField(label="Naran Divisaun (Portugues)", required=False)
    name_eng = forms.CharField(label="Naran Divisaun (Ingles)", required=True)
    overview_tet = forms.CharField(required=False,label="Overview Departamento (Tetum)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    overview_por = forms.CharField(required=False,label="Overview Departamento (Portugues)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    overview_eng = forms.CharField(required=False,label="Overview Departamento (Ingles)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    class Meta: 
        model = Division
        fields = ['department','name_tet', 'name_por', 'name_eng', 'overview_tet', 'overview_por','overview_eng', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name_tet', css_class='form-group col-md-3 mb-0'),
                Column('name_por', css_class='form-group col-md-3 mb-0'),
                Column('name_eng', css_class='form-group col-md-3 mb-0'),	
                Column('department', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('overview_tet', css_class='form-group col-md-4 mb-0'),
                Column('overview_por', css_class='form-group col-md-4 mb-0'),
                Column('overview_eng', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('image', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary" type="submit"><i class="bi bi-lock text-white"></i> Rai</button> """)
        )