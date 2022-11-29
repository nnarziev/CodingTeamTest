from django.urls import path

from restaurant.views import MenuListApiView

urlpatterns = [
    path('menu-list/', MenuListApiView.as_view(), name='menu-list')
]
