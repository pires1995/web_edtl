
from django import forms
from profiles.models import About, Employee, Position, Division
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class DateInput(forms.DateInput):
    input_type = 'date'

class AboutForm(forms.ModelForm):
	wwa_tet = forms.CharField(required=False,label="Who we are (Tetum)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	wwa_por = forms.CharField(required=False,label="Who we are (Portugues)",widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	wwa_eng = forms.CharField(required=False,label="Who we are (English)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	wwd_tet = forms.CharField(required=False,label="What we do (Tetun)",widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	wwd_por = forms.CharField(required=False,label="What we do (Portugues)",widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	wwd_eng = forms.CharField(required=False,label="What we do (English)",widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	class Meta:
		model = About
		fields = ['wwa_tet','wwa_por','wwa_eng','wwd_tet','wwd_por','wwd_eng']
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('wwa_tet', css_class='form-group col-md-4 mb-0'),
				Column('wwa_por', css_class='form-group col-md-4 mb-0'),
				Column('wwa_eng', css_class='form-group col-md-4 mb-0'),	
				css_class='form-row'
			),
			Row(
				Column('wwd_tet', css_class='form-group col-md-4 mb-0'),
				Column('wwd_por', css_class='form-group col-md-4 mb-0'),
				Column('wwd_eng', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit"><i class="bi bi-lock text-white"></i> Rai</button> """)
		)


class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ['first_name','last_name','sex','image', 'mobile', 'email']
	
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
			HTML(""" <button class="btn btn-primary" type="submit"><i class="bi bi-lock text-white"></i> Rai</button> """)
		)


class DivisionForm(forms.ModelForm):
	name_tet = forms.CharField(label="Naran Divisaun (Tetum)")
	name_por = forms.CharField(label="Naran Divisaun (Portugues)", required=False)
	name_eng = forms.CharField(label="Naran Divisaun (Ingles)", required=False)
	class Meta:
		model = Division
		fields = ['code','name_tet','name_por','name_eng']
	
	def __init__(self, *args, **kwargs):
		super(DivisionForm, self).__init__(*args, **kwargs)
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
		fields = ['division','employee','start_period',]
	
	def __init__(self, *args, **kwargs):
		super(PositionForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('division', css_class='form-group col-md-4 mb-0'),
				Column('employee', css_class='form-group col-md-4 mb-0'),	
				Column('start_period', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit"><i class="bi bi-lock text-white"></i> Rai</button> """)
		)