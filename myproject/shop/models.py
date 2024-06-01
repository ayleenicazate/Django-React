from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/')

    class Meta:
        db_table = "Products"
        verbose_name = "Products"
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return self.name

class Cart(models.Model):
    products = models.ManyToManyField(Product, through='CartItem')

    class Meta:
        db_table = "Cart"
        verbose_name = "Cart"
        verbose_name_plural = "Cart"

    def __str__(self) -> str:
        return self.products

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = "CartItem"
        verbose_name = "CartItem"
        verbose_name_plural = "CartItem"

    def __str__(self) -> str:
        return self.product