import os, hashlib
from uuid import uuid4

def path_and_rename_report(instance, filename):
	upload_to = 'report/pdf/{}/{}'.format(instance.pk,instance.hashed)
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(instance.pk,instance.hashed,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_report_image(instance, filename):
	upload_to = 'report/img/'
	field = 'report'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.pk, ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)