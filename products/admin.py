from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date', 'price', 'desc', 'summary')  # img_path 제외
    list_filter = ('pub_date',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_filter = ('pub_date',)
