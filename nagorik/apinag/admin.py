from django.contrib import admin

# Register your models here.

from .models import Issues, SubCategory, Category

admin.site.register(Issues)
admin.site.register(SubCategory)
admin.site.register(Category)
