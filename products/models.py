from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name="children",null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def sub_category(self):
        children_category = []
        for child in self.children:
            children_category.append(child)
        return children_category


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name="product_category")
    product_code = models.CharField(max_length=20)
    product_name = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_code
