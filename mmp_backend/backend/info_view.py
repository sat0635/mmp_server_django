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

def get(request):
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

