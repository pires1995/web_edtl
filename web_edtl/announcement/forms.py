

from django import forms
from announcement.models import Announcement
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML


class AnnoucementForm(forms.ModelForm):
    description_tet = forms.CharField(label="Content", widget=SummernoteWidget(
        attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    description_por = forms.CharField(label="Content", widget=SummernoteWidget(
        attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    description_eng = forms.CharField(label="Content", widget=SummernoteWidget(
        attrs={'summernote': {'width': '100%', 'height': '400px'}}))

    class Meta:
        model = Announcement
        fields = ['title_tet', 'title_por', 'title_eng',\
                   'description_tet','description_por','description_eng', 'image']

    def __init__(self, *args, **kwargs):
        super(AnnoucementForm, self).__init__(*args, **kwargs)
        # self.fields['image'].required = True
        self.helper = FormHelper()
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
                Column('image', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary text-white" type="submit"><i class="bi bi-lock text-white"></i> Save</button> """)
        )