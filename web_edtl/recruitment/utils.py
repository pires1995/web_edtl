import os, hashlib
from uuid import uuid4

def path_and_rename_vacancy_image(instance, filename):
	upload_to = 'recruitment/vacancy/img/{}/{}'.format(instance.pk,instance.hashed)
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(instance.pk,instance.hashed,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_vacancy_pdf(instance, filename):
	upload_to = 'report/vacancy/pdf/'
	field = 'vacancy'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.pk, ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_internships_image(instance, filename):
	upload_to = 'recruitment/internships/img/{}/{}'.format(instance.pk, instance.hashed)
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(instance.pk,instance.hashed,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_internships_pdf(instance, filename):
	upload_to = 'report/internships/pdf/'
	field = 'internships'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.pk, ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_volunteer_image(instance, filename):
	upload_to = 'recruitment/volunteer/img/{}/{}'.format(instance.pk, instance.hashed)
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(instance.pk,instance.hashed,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_volunteer_pdf(instance, filename):
	upload_to = 'report/volunteer/pdf/'
	field = 'volunteer'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.pk, ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)