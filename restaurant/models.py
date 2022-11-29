from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return '%s: %s' % (self.id, self.name)

    class Meta:
        verbose_name = 'Topping'
        verbose_name_plural = 'Toppings'


class FoodCategory(models.Model):
    name = models.CharField(max_length=20)
    is_publish = models.BooleanField()

    def __str__(self):
        return '%s: %s' % (self.id, self.name)

    class Meta:
        verbose_name = 'Food Category'
        verbose_name_plural = 'Food Categories'


class Food(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(FoodCategory, on_delete=models.SET_NULL, null=True, related_name='foods')
    description = models.TextField(blank=True)
    price = models.IntegerField()
    is_special = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_publish = models.BooleanField()
    toppings = models.ManyToManyField(Topping, related_name='foods')

    def __str__(self):
        return '%s: %s' % (self.id, self.name)

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'
