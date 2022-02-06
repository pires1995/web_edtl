from cProfile import label
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.db.models import Q
from django.contrib.auth.models import User, Group
from finance.models import Client
from custom.models import *
class DateInput(forms.DateInput):
	input_type = 'date'

class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = ['name','numero_kontador','email','mobile','address']
		labels = {
			'name': 'Naran Kliente',
			'numero_kontador': 'Numero Kontador',
			'mobile': 'Numeru Telefone',
			'address': 'Enderesu'
		}
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-4 mb-0'),
                Column('numero_kontador', css_class='form-group col-md-4 mb-0'),
                Column('address', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
			),
			Row(
                Column('email', css_class='form-group col-md-4 mb-0'),
				Column('mobile', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit"> Chave <i class="fa fa-save"></i></button> """)
		)