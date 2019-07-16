from django.contrib import admin
from .models import Store
from .models import Place
from .models import Coupon
# Register your models here.


admin.site.register(Coupon)
admin.site.register(Store)
admin.site.register(Place)
