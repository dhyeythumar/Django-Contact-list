from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.

from .models import Contact
from import_export.admin import ImportExportModelAdmin


class ContactAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'email', 'gender', 'info', 'phone')
    list_display_links = ('id', 'name')
    list_editable = ('info',)
    list_per_page = 10
    search_fields = ('name', 'email', 'gender', 'info', 'phone')
    list_filter = ('gender', 'date_added')


admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)
