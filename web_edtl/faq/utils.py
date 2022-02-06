import os, hashlib
from uuid import uuid4

def path_and_rename_faq_image(instance, filename):
	upload_to = 'faq/img/'
	field = 'faq'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.pk, ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)