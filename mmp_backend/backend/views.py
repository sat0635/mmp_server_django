from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Store
from backend.models import *
from .serializers import NearStoreSerializer

from django.http import HttpResponse
import json
import pprint
from math import sin,cos,sqrt,atan2,radians


def get_list_coupon(request,personID):
    queryset = Person.objects.all()
    result=queryset
    return HttpResponse(result)

def get_list_near_place(request,gpsx,gpsy):
    queryset = Place.objects.all()
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
    temp=(json.dumps(dict_list, ensure_ascii=False))
    return HttpResponse(temp)
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
    temp=(json.dumps(dict_list, ensure_ascii=False))
    return HttpResponse(temp)
def cal_distance(myLat, thisLat, dlon, dlat):
    a= sin(dlat / 2)**2 + cos(myLat) * cos(thisLat) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return c

