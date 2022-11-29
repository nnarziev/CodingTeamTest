from typing import List

from rest_framework import serializers

from restaurant.models import FoodCategory, Food


class FoodSerializer(serializers.ModelSerializer):
    toppings = serializers.SerializerMethodField()

    class Meta:
        model = Food
        fields = ('name', 'description', 'price', 'is_vegan', 'is_special', 'toppings')

    def get_toppings(self, obj: Food) -> List[str]:
        return [topping.name for topping in obj.toppings.all()]


class PublishedFoodsListSerializer(serializers.ModelSerializer):
    foods = serializers.SerializerMethodField()

    class Meta:
        model = FoodCategory
        fields = ('id', 'name', 'foods')

    def get_foods(self, obj: FoodCategory):
        request = self.context['request']
        is_vegan = request.query_params.get('is_vegan')
        is_special = request.query_params.get('is_special')
        toppings = request.query_params.getlist('toppings')

        foods_qs = obj.foods.prefetch_related('toppings').filter(is_publish=True)
        if is_vegan is not None:
            foods_qs = foods_qs.filter(is_vegan=is_vegan in ['True', 'true', '1', 'yes'])

        if is_special is not None:
            foods_qs = foods_qs.filter(is_special=is_special in ['True', 'true', '1', 'yes'])

        if toppings:
            foods_qs = foods_qs.filter(toppings__name__in=toppings).distinct()

        return FoodSerializer(foods_qs, many=True).data
