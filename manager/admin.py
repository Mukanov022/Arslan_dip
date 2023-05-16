import csv

from django.contrib import admin
from django.http import HttpResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from io import BytesIO
from django.conf import settings
from device_manager.settings import BASE_DIR
from .models import *


def export_to_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="export.pdf"'

    if settings.DEBUG:
        font_path = "http://127.0.0.1:8000" + settings.STATIC_URL + "dejavuserif.ttf"
    else:
        font_path = BASE_DIR / "static/vendor/assets/fonts/dejavuserif.ttf"

    pdfmetrics.registerFont(TTFont('DejaVuSans', font_path))

    pdf_buffer = BytesIO()
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    fields = modeladmin.list_display
    verbose_names = [modeladmin.model._meta.get_field(field).verbose_name for field in fields]

    cyrillic_style = ParagraphStyle(
        name='CyrillicStyle',
        parent=styles['Normal'],
        fontName='DejaVuSans',
    )

    data = [verbose_names]
    for obj in queryset:
        row = [
            Paragraph(str(getattr(obj, field)), cyrillic_style) for field in fields
        ]
        data.append(row)

    table = Table(data)
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'DejaVuSans'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table.setStyle(table_style)

    elements = [table]
    doc.build(elements)

    pdf = pdf_buffer.getvalue()
    pdf_buffer.close()
    response.write(pdf)

    return response


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
export_to_pdf.short_description = "Экспорт в PDF"


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ["serial_number", "device_name", "installing_date"]
    search_fields = ("device_name__startswith",)
    actions = [export_to_pdf, export_to_csv]


@admin.register(DeviceType)
class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ["type_name"]
    search_fields = ("type_name__startswith",)
    actions = [export_to_pdf, export_to_csv]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["personal_number", "first_name", "last_name", "role"]
    search_fields = ("last_name__startswith",)
    actions = [export_to_pdf, export_to_csv]


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ("name__startswith",)
    actions = [export_to_csv]


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ("desc__startswith",)
    actions = [export_to_pdf, export_to_csv]


@admin.register(Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ("country__startswith",)
    actions = [export_to_pdf, export_to_csv]


@admin.register(Properties)
class PropertiesAdmin(admin.ModelAdmin):
    list_display = ["id_device"]
    search_fields = ("id_settings__startswith",)
    actions = [export_to_pdf, export_to_csv]


@admin.register(Deportment)
class DeportmentAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ("name__startswith",)
    actions = [export_to_pdf, export_to_csv]
