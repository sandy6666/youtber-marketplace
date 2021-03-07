from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html

# Register your models here.


class YoutuberAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img width="40" src="{}"/>'.format(object.photo.url))

    list_display = ('id', 'first_name', 'last_name',
                    'myphoto', 'is_featured', 'created_at')
    list_display_links = ('first_name',)
    search_fields = ('first_name', 'camera_type')
    list_filter = ('created_at', 'city')
    list_editable = ('is_featured',)


admin.site.register(Youtuber, YoutuberAdmin)
