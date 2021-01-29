from django.urls import path
from . import views
from .models import Device,DeviceRecord
from django.conf.urls import url,handler404,handler500

# handler404 = "post.views.error404"
# handler500 = "post.views.error500"

app_name = 'post'
urlpatterns = [
    path('',views.devicecheck,name='devicecheck'),
    path('device_status/', views.device_status, name='device_status'),
    path('device_status/<int:device_id>/', views.devicecontorl, name='devicecontorl'),
    path('publish/<int:device_id>',views.publish, name='publish'),
    path('<int:device_id>',views.device, name='device')
    # path('<int:device_id/farmdata/',views.devicerecord,name='devicerecord')
    # feedin
]
