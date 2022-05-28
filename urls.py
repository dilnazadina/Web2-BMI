from django.contrib import admin
from django.urls import path, include
from users import views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path('index/', v.login_user, name="index"),
    path('bmi/', v.calculate, name="bmi"),
    path('physical/', v.physical_activity, name="physical"),
    path('eatHeart/', v.eatHeart, name="eatHeart"),
    path('healthy_weight/', v.healthy_weight, name="healthy_weight"),
    path('khowControl/', v.khowControl, name="khowControl"),
]

