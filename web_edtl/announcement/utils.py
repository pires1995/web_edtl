
import os
from uuid import uuid4
from datetime import datetime

def path_and_rename_announcement(instance, filename):
    upload_to = 'announcement/images/{}/{}/'.format(
        instance.date_posted.year, instance.date_posted.month)
    field = 'announcement'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}_{}_{}.{}'.format(
            field, instance.id, instance.id, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)
