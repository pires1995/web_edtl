
import os
from uuid import uuid4
from datetime import datetime

def path_and_rename_news(instance, filename):
    upload_to = 'news/images/{}/{}/'.format(
        instance.date_posted.year, instance.date_posted.month)
    field = 'news'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}_{}_{}.{}'.format(
            field, instance.id, instance.id, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)


def log_newsimage(path, newsid, imageid, description, image):
    log_data = str(newsid)+','+str(imageid)+','+str(description) + \
        ','+str(image)+','+str(datetime.datetime.now())+';\n'

    with open(path, 'a+') as f:
        f.write(log_data)
        f.close()
