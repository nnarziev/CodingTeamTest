from django.contrib import admin

from restaurant.models import Food, FoodCategory, Topping


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'description',
        'price',
        'is_special',
        'is_vegan',
        'is_publish',
        'toppings_count'
    )
    list_filter = ('category', 'is_special', 'is_vegan', 'is_publish')
    search_fields = ('description',)
    list_select_related = ('category',)

    def toppings_count(self, obj: Food):
        return obj.toppings.count()


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_publish',
    )
    list_filter = ('is_publish',)
    search_fields = ('name',)


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)
