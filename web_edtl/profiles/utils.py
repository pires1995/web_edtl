import os, hashlib
import datetime
from uuid import uuid4

def path_and_rename_about(instance, filename):
	upload_to = 'profile_files'
	field = 'about'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.pk, ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)
    
def path_and_rename_orgchart(instance, filename):
	upload_to = 'profile_files'
	field = 'orgchart'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.pk, ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)