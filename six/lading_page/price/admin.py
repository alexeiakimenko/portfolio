from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(PriceCard)
admin.site.register(PriceTable)