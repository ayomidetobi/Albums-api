from django.contrib import admin
from django.utils.html import format_html
from .models import Album, Track 

class TrackInline(admin.TabularInline):
    model = Track  
    extra = 1


class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        "artist_name",
        "album_name",
        "year_of_release",
        "ranking",
        "album_cover_display",
    )
    search_fields = ("artist_name", "album_name")
    list_filter = ("year_of_release", "ranking")
    inlines = [TrackInline]

    def album_cover_display(self, obj):
        if obj.album_cover:
            return format_html(
                '<img src="{}" width="50" height="50" />', obj.album_cover.url
            )
        return "No Image"

    album_cover_display.short_description = "Album Cover"


admin.site.register(Album, AlbumAdmin)
