from django.contrib import admin
from .models import Percent


class PercentAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'percent', 'percent_value', 'residual_value', 'value_increase')
    list_display_links = ('id', 'number')


admin.site.register(Percent, PercentAdmin)
