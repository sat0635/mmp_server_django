from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import viewsets
from .models import Store
from backend.models import *
from .serializers import VersionSerializer
from django.http import HttpResponse , JsonResponse
import json
import pprint
from math import sin,cos,sqrt,atan2,radians

class VersionViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset=Test.objects.all() 
    serializer_class=VersionSerializer


def get_list_coupon(request,personID):
    dict_list={}
    queryset = IndividualCoupon.objects.filter(PERSONID=personID)
    count=0
    for row in queryset:
        dictCoupon={}
        dictCoupon["PERSONID"]=personID       
        dictCoupon["STORENAME"]=row.STORENAME
        dictCoupon["NAME"]=row.NAME
        count+=1
        dict_list["key"+str(count)]=dictCoupon
    result=(json.dumps(dict_list,ensure_ascii=False))

    return HttpResponse(result)

def get_list_near_place(request,gpsx,gpsy):
    queryset = Place.objects.all()
    dict_list=[]
    dict_dict={}
    R=6373.0

    myLat=radians(float(gpsx))
    myLon=radians(float(gpsy))

    count=0
    for row in queryset:
        dictStore={}
        thisLat=radians(float(row.GPSX))
        thisLon=radians(float(row.GPSY))
        distance = cal_distance(myLat, thisLat, thisLat - myLat, thisLon - myLon)
        distance = distance * R
        #less than 10km
        if ( distance < 20.0):
            dictStore["GPSX"]=row.GPSX
            dictStore["GPSY"]=row.GPSY
            dictStore["DISTANCE"]=distance
            dictStore["LARG_CATE"]=row.LARG_CATE
            dictStore["MID_CATE"]=row.MID_CATE
            dictStore["SMALL_CATE"]=row.SMALL_CATE
            dictStore["NAME"]=row.NAME
            count+=1
            dict_list.append(dictStore)
    dict_dict["data"]=dict_list
    dict_temp={}
    dict_temp["gpsx"]="lopal"
    temp_list=[]
    temp_list.append(dict_temp)
    result=(json.dumps(temp_list, ensure_ascii=False))
    return JsonResponse(result)

def get_list_near_store(request,gpsx,gpsy):
    queryset = Store.objects.all()
    dict_list={}

    R=6373.0

    myLat=radians(float(gpsx))
    myLon=radians(float(gpsy))

    count=0
    for row in queryset:
        dictStore={}
        thisLat=radians(float(row.GPSX))
        thisLon=radians(float(row.GPSY))
        distance = cal_distance(myLat, thisLat, thisLat - myLat, thisLon - myLon)
        distance = distance * R
        #less than 10km
        if ( distance < 10.0):
            dictStore["GPSX"]=row.GPSX
            dictStore["GPSY"]=row.GPSY
            dictStore["DISTANCE"]=distance
            dictStore["LARG_CATE"]=row.LARG_CATE
            dictStore["MID_CATE"]=row.MID_CATE
            dictStore["SMALL_CATE"]=row.SMALL_CATE
            dictStore["NAME"]=row.NAME
            count+=1
            dict_list["key"+str(count)]=dictStore
    result=(json.dumps(dict_list, ensure_ascii=False))
    return HttpResponse(result)
def cal_distance(myLat, thisLat, dlon, dlat):
    a= sin(dlat / 2)**2 + cos(myLat) * cos(thisLat) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return c

