from django.contrib import admin
from .models import Computer, Ips, Region


class ComputerAdmin(admin.ModelAdmin):
    list_display = ('mgr_ip', 'person', 'purpose', 'update_time', 'left_time')


class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)


class IpsAdmin(admin.ModelAdmin):
    list_display = ('ip', 'person', 'purpose', 'update_time', 'left_time')

admin.site.register(Computer, ComputerAdmin)
admin.site.register(Ips, IpsAdmin)
admin.site.register(Region, RegionAdmin)