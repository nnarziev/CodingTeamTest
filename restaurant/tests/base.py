from rest_framework.test import APITestCase

from restaurant.models import FoodCategory, Topping, Food


class ApiBaseTest(APITestCase):
    def setUp(self) -> None:
        self.category1 = FoodCategory.objects.create(name='Category 1', is_publish=False)
        self.category2 = FoodCategory.objects.create(name='Category 2', is_publish=False)

        self.topping1 = Topping.objects.create(name='Topping 1')
        self.topping2 = Topping.objects.create(name='Topping 2')
        self.topping3 = Topping.objects.create(name='Topping 3')
        self.topping4 = Topping.objects.create(name='Topping 4')

        self.food1 = Food.objects.create(
            name='Food 1',
            category=self.category1,
            description='Dummy text',
            price=100,
            is_vegan=True,
            is_publish=True
        )
        self.food1.toppings.add(self.topping1, self.topping2)

        self.food2 = Food.objects.create(
            name='Food 2',
            category=self.category2,
            description='Dummy text',
            price=100,
            is_publish=True
        )
        self.food2.toppings.add(self.topping3, self.topping4)

        self.food3 = Food.objects.create(
            name='Food 3',
            category=self.category1,
            description='Dummy text',
            price=100,
            is_special=True,
            is_publish=True
        )
        self.food3.toppings.add(self.topping1)

        self.food4 = Food.objects.create(
            name='Food 4',
            category=self.category2,
            description='Dummy text',
            price=100,
            is_special=True,
            is_vegan=True,
            is_publish=True
        )
        self.food4.toppings.add(self.topping2, self.topping3, self.topping4)

        self.food5 = Food.objects.create(
            name='Food 5',
            category=self.category2,
            description='Dummy text',
            price=100,
            is_publish=False
        )
        self.food5.toppings.add(self.topping1, self.topping2, self.topping3, self.topping4)
