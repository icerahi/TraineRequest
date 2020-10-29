from django.contrib import admin

# Register your models here.
from accounts.models import Designation, Zone, Branch, Training_Title, Profile, TraineRequest


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    pass

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    pass

@admin.register(Branch)
class BranchZone(admin.ModelAdmin):
    pass

@admin.register(Training_Title)
class TitleAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(TraineRequest)
class TraineRequestAdmin(admin.ModelAdmin):
    list_display = ('employee_name','employee_id','designation','title','branch','zone')
    list_filter = ('title','branch','zone')