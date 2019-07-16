from django.contrib import admin
from .models import Store
from .models import Place
from .models import Coupon
from .models import IndividualCoupon
# Register your models here.

admin.site.register(IndividualCoupon)
admin.site.register(Coupon)
admin.site.register(Store)
admin.site.register(Place)
