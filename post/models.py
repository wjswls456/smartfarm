from django.db import models


class Device(models.Model):
    soil = models.CharField(max_length=200)
    def __str__(self):
        return self.soil
    # class Meta:
    #     db_table ="post_device"
class DeviceRecord(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    humidity = models.CharField(max_length=200)
    temperature = models.CharField(max_length=200)

    # class Meta:
    #     db_table ="post_devicerecord"
