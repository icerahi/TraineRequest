from import_export import resources
from django.contrib import admin

# Register your models here.
from accounts.models import Designation, Zone, Branch, Training_Title, Profile, TraineRequest
from import_export.admin import ImportExportModelAdmin

#designation
class DesignationResource(resources.ModelResource):
    class Meta:
        model=Designation
        fields=('name')

@admin.register(Designation)
class DesignationAdmin(ImportExportModelAdmin):
    search_fields = ('name',)
    resource_class = DesignationResource

#zone
class ZoneResource(resources.ModelResource):
    class Meta:
        model=Zone
        fields=('name')

@admin.register(Zone)
class ZoneAdmin(ImportExportModelAdmin):
    search_fields = ('name',)
    resource_class = ZoneResource

#Branch
class BranchResource(resources.ModelResource):
    class Meta:
        model=Branch
        fields=('zone__name','name')

@admin.register(Branch)
class BranchZone(ImportExportModelAdmin):
    resource_class = BranchResource
    list_display = ('name','zone',)
    list_filter = ('zone',)
    search_fields = ('name','zone__name')

#Title
class TitleResource(resources.ModelResource):
    class Meta:
        model=Training_Title
        fields=('name')

@admin.register(Training_Title)
class TitleAdmin(ImportExportModelAdmin):
    search_fields = ('name',)
    resource_class = TitleResource

#Profile
class ProfileResource(resources.ModelResource):
    class Meta:
        model=Profile
        fields=('user__username','designation__name','zone__name','branch__name','created',)

@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    list_display = ('user','designation','zone','branch',)
    search_fields = ('user__username','designation__name','zone__name','branch__name',)
    list_filter = ('designation','zone')
    resource_class = ProfileResource

#TraineRequest
class RequestResource(resources.ModelResource):
    class Meta:
        model=TraineRequest
        fields=('user__username','employee_id','employee_name','designation__name','title','zone__name','branch__name','created')

@admin.register(TraineRequest)
class TraineRequestAdmin(ImportExportModelAdmin):
    list_display = ('employee_name','employee_id','designation','title','branch','zone','created')
    list_filter = ('title','branch','zone')
    resource_class = RequestResource
    search_fields = ('employee_name','employee_id','designation__name','title__name','zone__name','branch__name')



admin.site.site_header = 'Training Need Assessment System (TNAS)'
admin.site.index_title = 'Islami Bank Traine Request System'
admin.site.site_title = 'Islami Bank Traine Request System'


