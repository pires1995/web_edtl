from django.db import models
import hashlib
from django.utils import timezone
from main.models import User
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from announcement.utils import path_and_rename_announcement



class Announcement(models.Model):
    model_name = "Announcement"
    title_tet = models.CharField(max_length=300, null=True)
    title_por = models.CharField(max_length=300, null=True)
    title_eng = models.CharField(max_length=300, null=True)
    description_tet = models.TextField(null=True)
    description_por = models.TextField(null=True, blank=True)
    description_eng = models.TextField(null=True, blank=True)
    image = ProcessedImageField(upload_to=path_and_rename_announcement, processors=[ResizeToFill(740, 500)],
                                format='JPEG', options={'quality': 60}, null=True, verbose_name="Cover Image")
    image_thumbnail = ImageSpecField(source='image',
                                            processors=[
                                                ResizeToFill(296, 197)],
                                            format='JPEG', options={'quality': 60})
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=False, null=True)
    is_send_notif = models.BooleanField(default=False, null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        template = '{0.title_tet} {0.title_eng}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Announcement, self).save(*args, **kwargs)