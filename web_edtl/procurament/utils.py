import os, hashlib
from uuid import uuid4

def path_and_rename_tender_image(instance, filename):
	upload_to = 'recruitment/tender/img/{}/{}'.format(instance.pk,instance.hashed)
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(instance.pk,instance.hashed,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_tender_pdf(instance, filename):
	upload_to = 'report/tender/pdf/'
	field = 'tender'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.pk, ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_guidelines_image(instance, filename):
	upload_to = 'recruitment/guidelines/img/{}/{}'.format(instance.pk, instance.hashed)
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(instance.pk,instance.hashed,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_guidelines_pdf(instance, filename):
	upload_to = 'report/guidelines/pdf/'
	field = 'guidelines'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.pk, ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)