from django.db import models
import hashlib
from django.utils import timezone
from main.models import User
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from news.utils import path_and_rename_news


class NewsCategory(models.Model):
    name = models.CharField(max_length=100)
    hashed = models.CharField(max_length=100, blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(NewsCategory, self).save(*args, **kwargs)


class News(models.Model):
    language = models.CharField(choices=[('Tetum', 'Tetum'), ('Portugues', 'Portugues'), (
        'English', 'English')], max_length=10, null=True, verbose_name="News Languages")
    news_category = models.ForeignKey(
        NewsCategory, on_delete=models.CASCADE, verbose_name="News Category", null=True)
    title = models.CharField(max_length=300, null=True)
    title_seo = models.CharField(max_length=350, null=True, blank=True)
    headline = models.TextField(null=True)
    content = models.TextField()
    image = ProcessedImageField(upload_to=path_and_rename_news, processors=[ResizeToFill(740, 500)],
                                format='JPEG', options={'quality': 60}, null=True, verbose_name="Cover Image")
    image_thumbnail = ImageSpecField(source='image',
                                            processors=[
                                                ResizeToFill(296, 197)],
                                            format='JPEG', options={'quality': 60})
    image_description = models.CharField(max_length=250, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author', null=True)
    is_active = models.BooleanField(default=True, null=True)
    is_sent = models.BooleanField(default=False, null=True)
    is_approved = models.BooleanField(default=False, null=True)
    is_reject = models.BooleanField(default=False, null=True)
    comment = models.CharField(max_length=300, null=True, blank=True)
    # entered_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
    #                                related_name='news_entered_by', verbose_name="Prenche husi")
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                                    related_name='news_approved_by', verbose_name="Aprova husi")
    entered_date = models.DateTimeField(auto_now_add=True, null=True)
    approved_date = models.DateTimeField(null=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        template = '{0.title}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(News, self).save(*args, **kwargs)


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE,
                             null=True, related_name="newsimage", verbose_name="Noticia")
    description_tet = models.CharField(max_length=200, null=True)
    description_por = models.CharField(max_length=200, null=True)
    description_eng = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    hashed = models.CharField(max_length=32, null=True)
    image = ProcessedImageField(upload_to=path_and_rename_news, processors=[ResizeToFill(740, 500)],
                                format='JPEG', options={'quality': 60}, null=True, verbose_name="Upload Imajen")
    image_thumbnail = ImageSpecField(source='image',
                                            processors=[
                                                ResizeToFill(296, 197)],
                                            format='JPEG', options={'quality': 60})

    def __str__(self):
        template = '{0.description_tet} | {0.news}'
        return template.format(self)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(NewsImage, self).save(*args, **kwargs)


class NewsUser(models.Model):
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
