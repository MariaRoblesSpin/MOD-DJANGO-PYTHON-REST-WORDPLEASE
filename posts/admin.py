from django.contrib import admin

from posts.models import Category
admin.site.register(Category)


from django.contrib import admin
from django.utils.safestring import mark_safe
from posts.models import Post


admin.site.site_title = 'WordPlease Admin System'
admin.site.site_header = 'WordPlease Admin System'
admin.site.index_title = 'WordPlease Admin System'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    # Customizando la administración del modelo Post
    list_select_related = ['user']
    list_display = ['id', 'get_img', 'title', 'text', 'fecha_publicacion', 'creation_date', 'modification_date']
    list_filter = ['categories', 'fecha_publicacion', 'user']
    search_fields = ['user', 'title', 'user__username']
    readonly_fields = ['get_img', 'creation_date', 'modification_date']
    fieldsets = [
        [None, {
            'fields': ['title', 'get_img', 'url']
        }],
        ['Properties', {
            'fields': ['text', 'categories', ]
        }],
        ['Description', {
            'fields': ['body']
        }],
        ['Dates', {
            'fields': ['creation_date', 'modification_date', 'fecha_publicacion'],
            'classes': ['collapse']
        }]
    ]

    def get_img(self, obj):
        return mark_safe('<img src="{0}" height="50">'.format(obj.url))

    get_img.short_description = 'Image'
    get_img.admin_order_field = 'name'
