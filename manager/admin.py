import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import *


def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'

    writer = csv.writer(response)
    fields = modeladmin.model._meta.fields

    # Create the matrix-like structure
    data = []
    header_row = [''] + [field.verbose_name for field in fields]
    data.append(header_row)

    for obj in queryset:
        data_row = [obj.pk] + [str(getattr(obj, field.name)) for field in fields]
        data.append(data_row)

    # Write the matrix-like structure
    for row in data:
        writer.writerow(row)

    return response


export_to_csv.short_description = "Экспорт в CSV"


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ["serial_number", "device_name", "installing_date"]
    search_fields = ("device_name__startswith",)
    actions = [export_to_csv]


@admin.register(DeviceType)
class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ["type_name"]
    search_fields = ("type_name__startswith",)
    actions = [export_to_csv]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["personal_number", "first_name", "last_name", "role"]
    search_fields = ("last_name__startswith",)
    actions = [export_to_csv]
    actions = [export_to_csv]


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ("name__startswith",)
    actions = [export_to_csv]


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ("desc__startswith",)
    actions = [export_to_csv]


@admin.register(Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ("country__startswith",)
    actions = [export_to_csv]


@admin.register(Properties)
class PropertiesAdmin(admin.ModelAdmin):
    list_display = ["id_device"]
    search_fields = ("id_settings__startswith",)
    actions = [export_to_csv]


@admin.register(Deportment)
class DeportmentAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ("name__startswith",)
    actions = [export_to_csv]
