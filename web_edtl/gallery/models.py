from django.db import models
import hashlib
from .utils import path_and_rename_album_image, path_and_rename_gallery_image, path_and_rename_banner
from main.models import User
from django.core.validators import FileExtensionValidator
from departments.models import Department
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)
    hashed = models.CharField(max_length=100, blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(GalleryCategory, self).save(*args, **kwargs)

class Album(models.Model):
    model_name="Album"
    category = models.ForeignKey(Department, on_delete=models.CASCADE)
    name_tet = models.CharField(max_length=254, null=False)
    name_por = models.CharField(max_length=254, null=True)
    name_eng = models.CharField(max_length=254, null=True)
    overview_tet = models.TextField(null=True, blank=True, verbose_name="Deskrisaun (Tetum) ")
    overview_por = models.TextField(null=True, blank=True, verbose_name="Deskrisaun (Portugues) ")
    overview_eng = models.TextField(null=True, blank=True, verbose_name="Deskrisaun (Ingles) ")
    image = models.ImageField(default='default.jpg', upload_to=path_and_rename_album_image, null=True, blank=True)
    image_thumbnail = ImageSpecField(source='image',
                        processors=[ResizeToFill(250,166)],
                        format='JPEG', options={'quality': 60})
    is_active = models.BooleanField(default=False, null=True)
    datetime = models.DateTimeField(auto_now_add=False, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)
    def __str__(self):
        template = '{0.name_tet}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Album, self).save(*args, **kwargs)

class Gallery(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, verbose_name="Album")
    overview_tet = models.TextField(null=True, blank=True, verbose_name='Deskrisaun (Tetum)' )
    overview_por = models.TextField(null=True, blank=True, verbose_name='Deskrisaun (Portugues)')
    overview_eng = models.TextField(null=True, blank=True, verbose_name='Deskrisaun (Ingles)')
    is_active = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to=path_and_rename_gallery_image, null=True, verbose_name="Upload Imajen")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    datetime = models.DateTimeField(auto_now_add=True,null=True)
    hashed = models.CharField(max_length=32, null=True)
    
    image_thumbnail = ImageSpecField(source='image',
                        processors=[ResizeToFill(296,197)],
                        format='JPEG', options={'quality': 60})

    def __str__(self):
        template = '{0.overview_tet} | {0.album}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Gallery, self).save(*args, **kwargs)


class Banner(models.Model):
    title_tet = models.CharField(max_length=200, null=True, blank=True)
    title_por = models.CharField(max_length=200, null=True, blank=True)
    title_eng = models.CharField(max_length=200)
    description_tet = models.CharField(max_length=200, null=True, blank=True)
    description_por = models.CharField(max_length=200, null=True, blank=True)
    description_eng = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(default='banner_default.jpg', upload_to=path_and_rename_banner, null=True, verbose_name="Upload Imajen")
    is_active = models.BooleanField(default=False, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    datetime = models.DateTimeField(null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        template = '{0.title_eng}'
        return template.format(self)
    
    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Banner, self).save(*args, **kwargs)

class VideoCategory(models.Model):
    name = models.CharField(max_length=100)
    hashed = models.CharField(max_length=100, blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(VideoCategory, self).save(*args, **kwargs)

class Video(models.Model):
    model_name="Video"
    video_type = models.ForeignKey(VideoCategory, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    title_tet = models.CharField(max_length=200, null=True, blank=True)
    title_por = models.CharField(max_length=200, null=True, blank=True)
    title_eng = models.CharField(max_length=200)
    url = models.CharField(max_length=300, null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    datetime = models.DateTimeField(auto_now_add=False, null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        template = '{0.title_eng}'
        return template.format(self)
    
    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Video, self).save(*args, **kwargs)