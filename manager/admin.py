from django.contrib import admin

from .models import *

admin.site.register(Device)
admin.site.register(DeviceType)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["personal_number", "first_name", "last_name", "role"]


admin.site.register(Settings)
admin.site.register(Role)
admin.site.register(Manufacture)
admin.site.register(Properties)
admin.site.register(Deportment)
