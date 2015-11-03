from django.contrib import admin
from .models import Client, Finance
from import_export.admin import ImportExportMixin, ExportActionModelAdmin


class ClientAdmin(ImportExportMixin, admin.ModelAdmin):
    list_filter = ['name', 'email']


class FinanceAdmin(ImportExportMixin, admin.ModelAdmin):
    list_filter = ['product_name',]

admin.site.register(Client, ClientAdmin)
admin.site.register(Finance, FinanceAdmin)
