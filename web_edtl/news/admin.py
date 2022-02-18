from django.contrib import admin
from .models import NewsUser, News, NewsCategory, NewsImage, SubscribeChoice
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_created',)


admin.site.register(NewsUser, NewsAdmin)
admin.site.register(News)
admin.site.register(NewsCategory)
admin.site.register(NewsImage)
admin.site.register(SubscribeChoice)
