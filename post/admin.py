from django.contrib import admin
from .models import  Device,DeviceRecord

class DeviceAdmin(admin.ModelAdmin):
    list_display =['id','soil']
    # raw_id_fields = ['device_id']

class DeviceRecordAdmin(admin.ModelAdmin):
    list_display = ['device_id','humidity','temperature']

admin.site.register(Device,DeviceAdmin)
admin.site.register(DeviceRecord,DeviceRecordAdmin)
# Register your models here.
