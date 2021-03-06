from django.http import JsonResponse,HttpResponse
from django.shortcuts import render, redirect
from django.core import serializers
from django.forms.models import model_to_dict
from .models import Device,DeviceRecord
import paho.mqtt.client as mqtt
import json
client_server = "server"
def device_status(request):
    latest_device_list = Device.objects.order_by('id')[:5]
    context = {'latest_device_list': latest_device_list}
    return render(request, 'device_status.html', context)

def devicecontorl(request,device_id):
    device_certified=Device.objects.filter(id=device_id)
    if device_certified:
        latest_devicerecord_list = DeviceRecord.objects.filter(device_id=device_id).order_by('-id')[:5]
    context = {'latest_devicerecord_list': latest_devicerecord_list,'device_id':device_id}
    return render(request, 'devicecontrol.html', context)

def publish(request,device_id):
    if request.method=='POST':
        topic = request.POST['topic']


        message = request.POST['message']


        id=request.POST['id']
        id = client_server + id
        mqttc = mqtt.Client(id)
        mqttc.connect("34.64.197.178",1883)
        mqttc.publish(topic,message, 0)
    return redirect('../device_status')



def device(request,device_id):
    if request.method=='GET':
        # device_data = list(Device.objects.filter(pk=device_id).values())
        device_data = Device.objects.get(pk=device_id)
        device_data_json=model_to_dict(device_data)
        print(device_data_json)
        return JsonResponse(device_data_json,safe=False)

    elif request.method=='POST':
        data = json.loads(request.body)
        print(data)
        if data['soildata']  == 0:
            DeviceRecord.objects.create(
            device_id = data['device_id'],
            humidity = data['humidity'],
            temperature = data['temperature'],
            )
        else:
            DeviceRecord.objects.create(
            device_id = data['device_id'],
            humidity = data['humidity'],
            temperature = data['temperature'],
            soildata= data['soildata']
            )
        return HttpResponse("well done")

def devicecheck(request):
    if request.method=='POST':
        data = json.loads(request.body)
        device_macaddress=Device(macaddress=data['macaddress'])
        devices_data=Device.objects.all()
        try:
            device_macaddress_data=devices_data.get(macaddress=data['macaddress'])
        except Device.DoesNotExist:
            Device.objects.create(
            macaddress = data['macaddress']
            )
            device_macaddress_data=devices_data.get(macaddress=data['macaddress'])
            macaddress_json=model_to_dict(device_macaddress_data)
            return JsonResponse(macaddress_json,safe=False)

        macaddress_json=model_to_dict(device_macaddress_data)
        return JsonResponse(macaddress_json,safe=False)


# def device_status(request):
#     if request.method=='GET':
#         return render(request,"testget.html")
#     elif request.method=='POST':
#         data = json.loads(request.body)
#         print(data)
#
#         # print(type(data['soil_name']))
#         # print(data['humidity'])
#         # print(type(data['humidity']))
#         if request.META['CONTENT_TYPE'] == "application/json":
#             print("json 보내고 있음")
#         # Farm(soil_name =data['soil_name']).save()
#         # Arduino(
#         # soil=data['soil']
#         # ).save()
#         DeviceRecord.objects.create(
#             device_id = data['device_id'],
#             humidity = data['humidity'],
#             temperature = data['temperature']
#             )
#         return render(request,"testget.html")



# def devicerecord(request,device_id):
