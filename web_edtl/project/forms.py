from django import forms
from project.models import Project, ProjectCategory, ProjectBudget, ProjectLocation, ProjectStatus, Fund
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from custom.models import Municipality, AdministrativePost, Village

class DateInput(forms.DateInput):
    input_type = 'date'

class OngoingProjectForm(forms.ModelForm):
    name = forms.CharField(label="Naran Projetu", required=True)
    description_tet = forms.CharField(required=False,label="Deskrisaun Tender (Tetum)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    description_por = forms.CharField(required=False,label="Deskrisaun Tender (Portugues)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    description_eng = forms.CharField(required=False,label="Deskrisaun Tender (Ingles)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    start_period = forms.DateField(widget=DateInput(), required=False)
    end_period = forms.DateField(widget=DateInput(), required=False)
    class Meta: 
        model = Project
        fields = ['name', 'year', 'project_status', 'project_category', \
              'description_tet', 'fund', 'typeofprocurament', 'company',
             'description_por','description_eng', \
                 'start_period', 'end_period']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-4 mb-0'),
                Column('project_category', css_class='form-group col-md-4 mb-0'),
                Column('project_status', css_class='form-group col-md-4 mb-0'),	
                css_class='form-row'
            ),
            Row(
                Column('start_period', css_class='form-group col-md-4 mb-0'),
                Column('end_period', css_class='form-group col-md-4 mb-0'),
                Column('fund', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('year', css_class='form-group col-md-4 mb-0'),
                Column('company', css_class='form-group col-md-4 mb-0'),
                Column('typeofprocurament', css_class='form-group col-md-4 mb-0'),
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

class NewProjectForm(forms.ModelForm):
    name = forms.CharField(label="Naran Projetu", required=True)
    description_tet = forms.CharField(required=False,label="Deskrisaun Tender (Tetum)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    description_por = forms.CharField(required=False,label="Deskrisaun Tender (Portugues)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    description_eng = forms.CharField(required=False,label="Deskrisaun Tender (Ingles)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))

    class Meta: 
        model = Project
        fields = ['name', 'year', 'project_status', 'project_category', \
              'description_tet', 'fund','description_por','description_eng', 'typeofprocurament']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-4 mb-0'),
                Column('project_category', css_class='form-group col-md-4 mb-0'),
                Column('project_status', css_class='form-group col-md-4 mb-0'),	
                css_class='form-row'
            ),
            Row(	
                Column('fund', css_class='form-group col-md-4 mb-0'),
                Column('year', css_class='form-group col-md-4 mb-0'),
                Column('typeofprocurament', css_class='form-group col-md-4 mb-0'),
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


class ProjectBudgetForm(forms.ModelForm):
    class Meta: 
        model = ProjectBudget
        fields = ['budget']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('budget', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary" type="submit"><i class="bi bi-lock text-white"></i> Rai</button> """)
        )


class ProjectLocationForm(forms.ModelForm):
	class Meta:
		model = ProjectLocation
		fields = ['municipality','administrativepost','village',\
			'latitude','longitude']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['administrativepost'].queryset = AdministrativePost.objects.none()
		self.fields['village'].queryset = Village.objects.none()
		
		if 'municipality' in self.data:
			try:
				municipality_id = int(self.data.get('municipality'))
				self.fields['administrativepost'].queryset = AdministrativePost.objects.filter(municipality_id=municipality_id).order_by('-id')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk and self.instance.municipality:
			self.fields['administrativepost'].queryset = self.instance.municipality.administrativepost_set.order_by('-id')

		if 'administrativepost' in self.data:
			try:
				administrativepost_id = int(self.data.get('administrativepost'))
				self.fields['village'].queryset = Village.objects.filter(administrativepost_id=administrativepost_id).order_by('-id')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk and self.instance.administrativepost:
			self.fields['village'].queryset = self.instance.administrativepost.village_set.order_by('name')