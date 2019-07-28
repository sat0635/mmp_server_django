from django.urls import path

from . import views

urlpatterns = [
    path('nearstore/<gpsx>/<gpsy>/', views.get_list_near_store),
    path('nearplace/<gpsx>/<gpsy>/', views.get_list_near_place),
    path('coupon/<userid>/', views.get_list_coupon),
    path('picture/', views.get_list_picture),
    path('event/', views.get_list_event),
    path('comment/<pictureid>/', views.get_list_comment),
    path('insertuser/<userid>/', views.insert_user),
    path('heart/<pictureid>/',views.send_heart),
    path('getheart/<pictureid>/',views.get_heart),
]
