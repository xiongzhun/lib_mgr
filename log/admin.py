from django.contrib import admin
from .models import Log_type, Log


class LogAdmin(admin.ModelAdmin):
    list_display = ('title', 'person', 'start_time', 'region', 'detail')


class Log_typeAdmin(admin.ModelAdmin):
    list_display = ('type',)


admin.site.register(Log, LogAdmin)
admin.site.register(Log_type, Log_typeAdmin)

