from django.contrib import admin
from .models import Store
from .models import Place
from .models import Coupon
from .models import IndividualCoupon
from .models import Test
from .models import Picture
# Register your models here.

admin.site.register(IndividualCoupon)
admin.site.register(Coupon)
admin.site.register(Store)
admin.site.register(Place)
admin.site.register(Test)
admin.site.register(Picture)
