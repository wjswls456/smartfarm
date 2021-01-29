from django.db import models


class Device(models.Model):
    soil = models.CharField(max_length=200,default="nodata" , blank=True, null=False)
    macaddress = models.CharField(max_length=200,default="nothing" , blank=True, null=False)

    def __str__(self):
        return self.macaddress
    # class Meta:
    #     db_table ="post_device"
class DeviceRecord(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    humidity = models.CharField(max_length=200,null=True)
    temperature = models.CharField(max_length=200,null=True)
    # soildata = models.CharField(max_length=200,null=True)




    # class Meta:
    #     db_table ="post_devicerecord"
