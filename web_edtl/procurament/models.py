from django.db import models
import hashlib
from .utils import path_and_rename_tender_pdf, path_and_rename_tender_image, path_and_rename_guidelines_pdf,path_and_rename_guidelines_image, path_and_rename_policy_pdf
from main.models import User
from django.core.validators import FileExtensionValidator

class Tender(models.Model):
    title_tet = models.CharField(max_length=254, null=False)
    title_por = models.CharField(max_length=254, null=True)
    title_eng = models.CharField(max_length=254, null=True)
    description_tet = models.TextField(null=True, blank=True)
    description_por = models.TextField(null=True, blank=True)
    description_eng = models.TextField(null=True, blank=True)
    start_period = models.DateField(null=True, blank=True)
    end_period = models.DateField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to=path_and_rename_tender_image, null=True, blank=True)
    file = models.FileField(upload_to=path_and_rename_tender_pdf,
                            validators=[FileExtensionValidator(allowed_extensions=['pdf', 'csv', 'doc', 'docx', 'xls', 'xlsx'])])
    is_active = models.BooleanField(default=False, null=True)
    is_send_notif = models.BooleanField(default=False, null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)
    def __str__(self):
        template = '{0.title_tet}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Tender, self).save(*args, **kwargs)

class Guidelines(models.Model):
    title_tet = models.CharField(max_length=254, null=False)
    title_por = models.CharField(max_length=254, null=True)
    title_eng = models.CharField(max_length=254, null=True)
    description_tet = models.TextField(null=True, blank=True)
    description_por = models.TextField(null=True, blank=True)
    description_eng = models.TextField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to=path_and_rename_guidelines_image, null=True, blank=True)
    file = models.FileField(upload_to=path_and_rename_guidelines_pdf,
                            validators=[FileExtensionValidator(allowed_extensions=['pdf', 'csv', 'doc', 'docx', 'xls', 'xlsx'])])
    is_active = models.BooleanField(default=False, null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)
    def __str__(self):
        template = '{0.title_tet}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Guidelines, self).save(*args, **kwargs)

class Policy(models.Model):
    title_tet = models.CharField(max_length=254, null=False)
    title_por = models.CharField(max_length=254, null=True)
    title_eng = models.CharField(max_length=254, null=True)
    description_tet = models.TextField(null=True, blank=True)
    description_por = models.TextField(null=True, blank=True)
    description_eng = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to=path_and_rename_policy_pdf,
                            validators=[FileExtensionValidator(allowed_extensions=['pdf', 'csv', 'doc', 'docx', 'xls', 'xlsx'])])
    is_active = models.BooleanField(default=False, null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)
    def __str__(self):
        template = '{0.title_tet}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Policy, self).save(*args, **kwargs)