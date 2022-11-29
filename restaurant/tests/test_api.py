from rest_framework.status import HTTP_200_OK

from restaurant.models import FoodCategory
from restaurant.tests.base import ApiBaseTest

MENU_LIST_API_URL = '/restaurant/menu-list/'


class TestMenuListView(ApiBaseTest):

    def test_menu_list_success(self) -> None:
        res = self.client.get(MENU_LIST_API_URL)
        self.assertEqual(res.status_code, HTTP_200_OK)

    def test_menu_list_categories_count(self) -> None:
        res = self.client.get(MENU_LIST_API_URL)
        data = res.json()
        categories_count = FoodCategory.objects.count()
        self.assertEqual(len(data), categories_count)

    def test_menu_list_foods_count(self) -> None:
        res = self.client.get(MENU_LIST_API_URL)
        data = res.json()

        for category in data:
            category_obj = FoodCategory.objects.get(id=category['id'])
            self.assertEqual(len(category['foods']), category_obj.foods.filter(is_publish=True).count())

    def test_menu_list_for_not_published_foods(self) -> None:
        '''
        Test the case where food5 with is_publish=False not it the response
        '''
        res = self.client.get(MENU_LIST_API_URL)
        data = res.json()
        for category in data:
            food_names = [i['name'] for i in category['foods']]
            self.assertNotIn(self.food5.name, food_names)

    def test_menu_list_with_toppings(self) -> None:
        '''
        Test if any of topping from toppings is in each food's toppings
        '''
        toppings = ['Topping 1', 'Topping 2']
        res = self.client.get(MENU_LIST_API_URL, {'toppings': toppings})
        data = res.json()
        for category in data:
            for food in category['foods']:
                self.assertEqual(any(i in food['toppings'] for i in toppings), True)

    def test_menu_list_with_is_special(self) -> None:
        res = self.client.get(MENU_LIST_API_URL, {'is_special': 'true'})
        data = res.json()
        for category in data:
            for food in category['foods']:
                self.assertEqual(food['is_special'], True)

    def test_menu_list_with_is_vegan(self) -> None:
        res = self.client.get(MENU_LIST_API_URL, {'is_vegan': 'true'})
        data = res.json()
        for category in data:
            for food in category['foods']:
                self.assertEqual(food['is_vegan'], True)

    def test_menu_list_with_is_special_and_is_vegan(self) -> None:
        res = self.client.get(MENU_LIST_API_URL, {'is_special': 'true', 'is_vegan': 'true'})
        data = res.json()
        for category in data:
            for food in category['foods']:
                self.assertEqual(food['is_special'], True)
                self.assertEqual(food['is_vegan'], True)
