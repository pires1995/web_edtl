import os, hashlib
import datetime
from uuid import uuid4

def path_and_rename_department(instance, filename):
	upload_to = 'departments'
	field = 'department'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.pk, ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)