<<<<<<< HEAD
from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


# Register your models here.


class CmsAdmin(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_text', 'cms_css', 'get_img')
    list_editable = ('cms_css',)
    fields = ('cms_title', 'cms_text', 'cms_css', 'cms_img', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        return mark_safe(f'<img src={obj.cms_img.url} width="80">')


admin.site.register(CmsSlider, CmsAdmin)
=======
from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


# Register your models here.


class CmsAdmin(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_text', 'cms_css', 'get_img')
    list_editable = ('cms_css',)
    fields = ('cms_title', 'cms_text', 'cms_css', 'cms_img', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        return mark_safe(f'<img src={obj.cms_img.url} width="80">')


admin.site.register(CmsSlider, CmsAdmin)
>>>>>>> c56e1a6cee1fb286d87fdf677c9758e9a101d523
