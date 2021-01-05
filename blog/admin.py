from django.contrib import admin
from .models import Post, Genre

from mptt.admin import DraggableMPTTAdmin

# Register your models here.
admin.site.register(Post)

#admin.site.register(Genre)
admin.site.register(
    Genre,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)