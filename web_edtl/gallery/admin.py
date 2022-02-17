from django.contrib import admin
from gallery.models import Album, Gallery, GalleryCategory, Banner, VideoCategory, Video

# Register your models here.
admin.site.register(Album)
admin.site.register(Gallery)
admin.site.register(GalleryCategory)
admin.site.register(Banner)
admin.site.register(VideoCategory)
admin.site.register(Video)