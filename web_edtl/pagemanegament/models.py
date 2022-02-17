from django.db import models
import hashlib
from main.models import User

class PageManegament(models.Model):
    name = models.CharField(max_length=254, null=False)
    description_tet = models.TextField(null=True, blank=True)
    description_por = models.TextField(null=True, blank=True)
    description_eng = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)
    def __str__(self):
        template = '{0.name_tet}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(PageManegament, self).save(*args, **kwargs)
