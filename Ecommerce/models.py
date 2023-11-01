from django.db import models
from django.urls import reverse

# from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


# class OrderItem(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     ordered = models.BooleanField(default=False)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)

#     def __str__(self):
#         return f"{self.quantity} of {self.item.title}"

#     def get_total_item_price(self):
#         return self.quantity * self.item.price

#     def get_total_discount_item_price(self):
#         return self.quantity * self.item.discount_price

#     def get_amount_saved(self):
#         return self.get_total_item_price() - self.get_total_discount_item_price()

#     def get_final_price(self):
#         if self.item.discount_price:
#             return self.get_total_discount_item_price()
#         return self.get_total_item_price()


# class Category(models.Model):
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, unique=True)

#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'category'
#         verbose_name_plural = 'categories'

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('shop:product_list_by_category', args=[self.slug])


# class Product(models.Model):
#     category = models.ForeignKey(Category, related_name='products',
#                                  on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True)
#     image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ('name',)
#         index_together = (('id', 'slug'),)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('shop:product_detail', args=[self.id, self.slug])



# class Order(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     address = models.CharField(max_length=250)
#     postal_code = models.CharField(max_length=20)
#     city = models.CharField(max_length=100)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     paid = models.BooleanField(default=False)

#     class Meta:
#         ordering = ('-created',)

#     def __str__(self):
#         return 'Order {}'.format(self.id)

#     def get_total_cost(self):
#         return sum(item.get_cost() for item in self.items.all())

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return '{}'.format(self.id)

#     def get_cost(self):
#         return self.price * self.quantity

# class Coupon(models.Model):
#     code = models.CharField(max_length=50, unique=True)
#     valid_from = models.DateTimeField()
#     valid_to = models.DateTimeField()
#     discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
#     active = models.BooleanField()

#     def __str__(self):
#         return self.code
