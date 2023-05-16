from django.contrib import admin

from .models import *


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ["serial_number","device_name","installing_date"]
    search_fields = ("device_name__startswith",)


@admin.register(DeviceType)
class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ["type_name"]
    search_fields = ("type_name__startswith",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["personal_number", "first_name", "last_name", "role"]
    search_fields = ("last_name__startswith",)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ("name__startswith",)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ("desc__startswith",)


@admin.register(Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ("country__startswith",)


@admin.register(Properties)
class PropertiesAdmin(admin.ModelAdmin):
    list_display = ["id_device"]
    search_fields = ("id_settings__startswith",)


@admin.register(Deportment)
class DeportmentAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ("name__startswith",)
