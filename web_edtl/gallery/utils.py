import os, hashlib
from uuid import uuid4

def path_and_rename_album_image(instance, filename):
	upload_to = 'album/img/'
	field = 'album'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.pk, ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_gallery_image(instance, filename):
	upload_to = 'gallery/img/'
	field = 'gallery'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.pk, ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)