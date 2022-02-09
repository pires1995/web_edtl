from django.contrib import admin
from gallery.models import Album, Gallery, GalleryCategory

# Register your models here.
admin.site.register(Album)
admin.site.register(Gallery)
admin.site.register(GalleryCategory)