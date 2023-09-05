<<<<<<< HEAD
from django.contrib import admin
from .models import *


class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_dt', 'comment_text')
    readonly_fields = ('comment_dt',)
    extra = 0


class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    list_display_links = ('order_name',)
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    list_editable = ('order_status', 'order_phone')
    list_filter = ('order_status',)
    fields = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    readonly_fields = ('order_dt', 'id')
    inlines = [Comment]
    list_per_page = 5

admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)

# Register your models here.
=======
from django.contrib import admin
from .models import *


class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_dt', 'comment_text')
    readonly_fields = ('comment_dt',)
    extra = 0


class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    list_display_links = ('order_name',)
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    list_editable = ('order_status', 'order_phone')
    list_filter = ('order_status',)
    fields = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    readonly_fields = ('order_dt', 'id')
    inlines = [Comment]
    list_per_page = 5

admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)

# Register your models here.
>>>>>>> c56e1a6cee1fb286d87fdf677c9758e9a101d523
