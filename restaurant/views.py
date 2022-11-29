from rest_framework.generics import ListAPIView

from restaurant.models import FoodCategory
from restaurant.serializers import PublishedFoodsListSerializer


class MenuListApiView(ListAPIView):
    queryset = FoodCategory.objects.all()
    serializer_class = PublishedFoodsListSerializer
