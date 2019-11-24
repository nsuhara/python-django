from django.contrib import admin

from django_model.models import UsdJpy


@admin.register(UsdJpy)
class UsdJpyAdmin(admin.ModelAdmin):
    fields = ('time_stamp', 'usd_jpy')
    list_display = ('id', 'time_stamp', 'usd_jpy')
