from django.contrib import admin

# Register your models here.
from accounts.models import Designation, Zone, Branch, Training_Title, Profile, TraineRequest
from import_export.admin import ImportExportModelAdmin

@admin.register(Designation)
class DesignationAdmin(ImportExportModelAdmin):
    pass

@admin.register(Zone)
class ZoneAdmin(ImportExportModelAdmin):
    pass

@admin.register(Branch)
class BranchZone(ImportExportModelAdmin):
    pass

@admin.register(Training_Title)
class TitleAdmin(ImportExportModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    pass

@admin.register(TraineRequest)
class TraineRequestAdmin(ImportExportModelAdmin):
    list_display = ('employee_name','employee_id','designation','title','branch','zone')
    list_filter = ('title','branch','zone')



admin.site.site_header = 'Islami Bank Traine Request System'
admin.site.index_title = 'Islami Bank Traine Request System'
admin.site.site_title = 'Islami Bank Traine Request System'


