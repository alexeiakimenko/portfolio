from django.contrib import admin

from .models import *
<<<<<<< HEAD
from django import forms
from django.utils.safestring import mark_safe


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'
=======
>>>>>>> parent of 7574f18 (change)


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
    list_display = ('id', 'title', 'time_created', 'time_update', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content')
    readonly_fields = ('time_created', 'time_update')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_created')
    fields = (
    'title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_created', 'time_update')
    readonly_fields = ('get_html_photo', 'is_published', 'time_created', 'time_update')
    save_on_top = True

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="70">')

    get_html_photo.short_description = 'Миниатюра'


class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CatAdmin)
