
from django import forms
from profiles.models import About, Service, Employee, Position, Division
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class DateInput(forms.DateInput):
    input_type = 'date'

class AboutForm(forms.ModelForm):
	background_tet = forms.CharField(required=False,label="Background (Tetum)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	background_por = forms.CharField(required=False,label="Background (Portugues)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	background_eng = forms.CharField(required=False,label="Background (English)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	mission_tet = forms.CharField(required=False,label="Mission (Tetum)",widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	mission_por = forms.CharField(required=False,label="Mission (Portugues)",widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	mission_eng = forms.CharField(required=False,label="Mission (English)",widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	vision_tet = forms.CharField(required=False,label="Vision (Tetum)",widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	vision_por = forms.CharField(required=False,label="Vision (Portugues)",widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	vision_eng = forms.CharField(required=False,label="Vision (English)",widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	values_tet = forms.CharField(required=False,label="Values (Tetum)",widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	values_por = forms.CharField(required=False,label="Values (Portugues)",widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	values_eng = forms.CharField(required=False,label="Values (English)",widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	objective_tet = forms.CharField(required=False,label="Objective (Tetum)",widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	objective_por = forms.CharField(required=False,label="Objective (Portugues)",widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	objective_eng = forms.CharField(required=False,label="Objective (English)",widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	
	class Meta:
		model = About
		fields = ['background_tet','background_por','background_eng','mission_tet','mission_por','mission_eng','vision_tet', 'vision_por', 'vision_eng',\
			'objective_tet', 'objective_por', 'objective_eng', 'image','values_tet','values_por','values_eng']
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('background_tet', css_class='form-group col-md-4 mb-0'),
				Column('background_por', css_class='form-group col-md-4 mb-0'),
				Column('background_eng', css_class='form-group col-md-4 mb-0'),	
				css_class='form-row'
			),
			Row(
				Column('mission_tet', css_class='form-group col-md-4 mb-0'),
				Column('mission_por', css_class='form-group col-md-4 mb-0'),
				Column('mission_eng', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('vision_tet', css_class='form-group col-md-4 mb-0'),
				Column('vision_por', css_class='form-group col-md-4 mb-0'),
				Column('vision_eng', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('objective_tet', css_class='form-group col-md-4 mb-0'),
				Column('objective_por', css_class='form-group col-md-4 mb-0'),
				Column('objective_eng', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('values_tet', css_class='form-group col-md-4 mb-0'),
				Column('values_por', css_class='form-group col-md-4 mb-0'),
				Column('values_eng', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('image', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit"><i class="bi bi-lock text-white"></i> Rai</button> """)
		)



class ServiceForm(forms.ModelForm):
	class Meta:
		model = Service
		fields = ['title_tet','title_por','title_eng','description_tet','description_por','description_eng']
	
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
			# Row(
			# 	Column('image', css_class='form-group col-md-12 mb-0'),
			# 	css_class='form-row'
			# ),
			HTML(""" <button class="btn btn-primary" type="submit"><i class="bi bi-lock text-white"></i> Rai</button> """)
		)


class EmployeeForm(forms.ModelForm):
	resume = forms.CharField(required=False,label="Resume", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	class Meta:
		model = Employee
		fields = ['first_name','last_name','sex','image', 'mobile', 'email', 'resume']
	
	def __init__(self, *args, **kwargs):
		super(EmployeeForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('first_name', css_class='form-group col-md-5 mb-0'),
				Column('last_name', css_class='form-group col-md-5 mb-0'),	
				Column('sex', css_class='form-group col-md-2 mb-0'),	
				css_class='form-row'
			),
			Row(
				Column('mobile', css_class='form-group col-md-4 mb-0'),
				Column('email', css_class='form-group col-md-4 mb-0'),
				Column('image', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('resume', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit"><i class="bi bi-lock text-white"></i> Rai</button> """)
		)


class DivisionProfileForm(forms.ModelForm):
	name_tet = forms.CharField(label="Naran Divisaun (Tetum)")
	name_por = forms.CharField(label="Naran Divisaun (Portugues)", required=False)
	name_eng = forms.CharField(label="Naran Divisaun (Ingles)", required=False)
	class Meta:
		model = Division
		fields = ['code','name_tet','name_por','name_eng']
	
	def __init__(self, *args, **kwargs):
		super(DivisionProfileForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('code', css_class='form-group col-md-3 mb-0'),
				Column('name_tet', css_class='form-group col-md-3 mb-0'),	
				Column('name_por', css_class='form-group col-md-3 mb-0'),	
				Column('name_eng', css_class='form-group col-md-3 mb-0'),	
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit"><i class="bi bi-lock text-white"></i> Rai</button> """)
		)

class PositionForm(forms.ModelForm):
	start_period = forms.DateField(widget=DateInput(), required=False)
	class Meta:
		model = Position
		fields = ['position','employee','group']
	
	def __init__(self, *args, **kwargs):
		super(PositionForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('position', css_class='form-group col-md-4 mb-0'),
				Column('employee', css_class='form-group col-md-4 mb-0'),	
				Column('group', css_class='form-group col-md-4 mb-0'),	
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit"><i class="bi bi-lock text-white"></i> Rai</button> """)
		)