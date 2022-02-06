from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.db.models import Q, fields
from django.contrib.auth.models import User
from gallery.models import  Album, Gallery
from departments.models import Department
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class AlbumComments(forms.ModelForm):
	comments = forms.CharField(label='Komentariu')
	class Meta:
		model = Album
		fields = ['comments']

class DateInput(forms.DateInput):
	input_type = 'date'

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name_tet', 'name_por', 'name_eng', 'category','overview_tet','overview_por','overview_eng','image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Department.objects.all()
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name_tet', css_class='form-group col-md-3 mb-0'),
                Column('name_por', css_class='form-group col-md-3 mb-0'),
                Column('name_eng', css_class='form-group col-md-3 mb-0'),	
                Column('category', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('overview_tet', css_class='form-group col-md-3 mb-0'),
                Column('overview_por', css_class='form-group col-md-3 mb-0'),
                Column('overview_eng', css_class='form-group col-md-3 mb-0'),
                Column('image', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary" type="submit"><i class="bi bi-lock text-white"></i> Rai</button> """)
        )

class GalleryForm(forms.ModelForm):
    image = forms.FileField(label="Upload image", required=True,
                            widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Gallery
        fields = ['overview_tet','overview_por','overview_eng','image']
    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('image', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('overview_tet', css_class='form-group col-md-4 mb-0'),
                Column('overview_por', css_class='form-group col-md-4 mb-0'),
                Column('overview_eng', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            HTML(
                """ <a class="btn btn-secondary" href="{% url 'admin-album-list' %}"><i class="fa fa-close"></i> Fila</a> """),
            HTML(""" <button class="btn btn-primary" type="submit"> Rai <i class="fa fa-save"></i></button> """)
        )
