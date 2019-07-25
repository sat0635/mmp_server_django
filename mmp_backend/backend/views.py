from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import viewsets
from .models import Store
from backend.models import *
from django.http import HttpResponse , JsonResponse
import json
from math import sin,cos,sqrt,atan2,radians
from functools import wraps
def insert_user(request, userid):
    instance = User(USERID=userid)
    instance.save()

def get_list_event(request):
    queryset = Event.objects.all()
    dict_list=[]
    for row in queryset:
        dictEvent={}
        dictEvent["TITLE"]=row.TITLE
        dictEvent["CONTENT"]=row.CONTENT
        dictEvent["IMAGE"]="http://106.10.35.40:8000/media/"+str(row.IMAGE)
        print(row.start_time)
        dict_list.append(dictEvent)
    result=(json.dumps(dict_list, ensure_ascii=False).encode('utf8') )
    return HttpResponse(result, content_type=u"application/json; charset=utf-8")
def get_list_picture(request):
    queryset = Picture.objects.all()
    dict_list=[]
    for row in queryset:
        dictPicture={}
        dictPicture["TITLE"]=row.TITLE
        dictPicture["CONTENT"]=row.CONTENT
        dictPicture["IMAGE"]="http://106.10.35.40:8000/media/"+str(row.IMAGE)
        dict_list.append(dictPicture)
    result=(json.dumps(dict_list, ensure_ascii=False).encode('utf8') )
    return HttpResponse(result, content_type=u"application/json; charset=utf-8")

def get_list_coupon(request,userid):
    dict_list=[]
    queryset = IndividualCoupon.objects.filter(USERID=userid)
    for row in queryset:
        instance = Coupon.objects.filter(id=row.COUPONID)
	
        for row2 in instance:
            dictCoupon={}
            dictCoupon["STORENAME"]=row2.STORENAME
            dictCoupon["NAME"]=row2.NAME
            dictCoupon["IMAGE"]="http://106.10.35.40:8000/media/"+str(row2.IMAGE)
            dictCoupon["COUPONID"]=row.COUPONID
            dict_list.append(dictCoupon)

    result=(json.dumps(dict_list, ensure_ascii=False).encode('utf8') )
    return HttpResponse(result, content_type=u"application/json; charset=utf-8")

def get_list_near_place(request,gpsx,gpsy):
    queryset = Place.objects.all()
    dict_list=[]
    R=6373.0

    myLat=radians(float(gpsx))
    myLon=radians(float(gpsy))

    count=0
    for row in queryset:
        dictPlace={}
        thisLat=radians(float(row.GPSX))
        thisLon=radians(float(row.GPSY))
        distance = cal_distance(myLat, thisLat, thisLat - myLat, thisLon - myLon)
        distance = distance * R
        #less than 20km
        if ( distance < 20.0):
            dictPlace["GPSX"]=row.GPSX
            dictPlace["GPSY"]=row.GPSY
            dictPlace["DISTANCE"]=distance
            dictPlace["LARG_CATE"]=row.LARG_CATE
            dictPlace["MID_CATE"]=row.MID_CATE
            dictPlace["SMALL_CATE"]=row.SMALL_CATE
            dictPlace["NAME"]=row.NAME
            dist=str(distance).split(".")[0]+"."+str(distance).split(".")[1][:3]
            dictPlace["DISTANCE"]=dist+"km"
            dictPlace["IMAGE"]="http://106.10.35.40:8000/media/"+str(row.IMAGE)
            dict_list.append(dictPlace)
    result=(json.dumps(dict_list, ensure_ascii=False).encode('utf8') )
    return HttpResponse(result, content_type=u"application/json; charset=utf-8")

def get_list_near_store(request,gpsx,gpsy):
    queryset = Store.objects.all()
    dict_list=[]

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
        #less than 20km
        if ( distance < 20.0):
            dictStore["GPSX"]=row.GPSX
            dictStore["GPSY"]=row.GPSY
            dictStore["DISTANCE"]=distance
            dictStore["LARG_CATE"]=row.LARG_CATE
            dictStore["MID_CATE"]=row.MID_CATE
            dictStore["SMALL_CATE"]=row.SMALL_CATE
            dictStore["NAME"]=row.NAME
            dist=str(distance).split(".")[0]+"."+str(distance).split(".")[1][:3]
            dictStore["DISTANCE"]=dist+"km"
            dictStore["IMAGE"]="http://106.10.35.40:8000/media/"+str(row.IMAGE)
            dict_list.append(dictStore)
    result=(json.dumps(dict_list, ensure_ascii=False).encode('utf8') )
    return HttpResponse(result, content_type=u"application/json; charset=utf-8")

def cal_distance(myLat, thisLat, dlon, dlat):
    a= sin(dlat / 2)**2 + cos(myLat) * cos(thisLat) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return c

