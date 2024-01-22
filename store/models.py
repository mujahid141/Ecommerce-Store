from django.db import models
class Promotions(models.Model):
    description = models.CharField(max_length=225)
    discount = models.FloatField()
    def __str__(self) -> str:
        return self.description

class Collection(models.Model):
    Name = models.CharField(max_length=225)
    description = models.TextField()
    def __str__(self) -> str:
        return self.Name

    
    
    

class Product(models.Model):
    p_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Adjust max_digits based on your requirements
    inventory = models.IntegerField()  # Corrected typo in field name
    last_update = models.DateTimeField(auto_now_add=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    promotions = models.ManyToManyField(Promotions)

    def __str__(self) -> str:
        return self.title

class Customer(models.Model):
    MEMBERSHIP_B = 'B'
    MEMBERSHIP_S = 'S'
    MEMBERSHIP_G = 'G'
    
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_B, 'Bronze'),
        (MEMBERSHIP_S, 'Silver'),
        (MEMBERSHIP_G, 'Gold'),
    ]
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField(max_length=20)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_B)
    def __str__(self) -> str:
        return self.first_name

    
class Order(models.Model):
    PAYMENT_P ='P'
    PAYMENT_C ='C'
    PAYMENT_F ='F'
    PAYMENT_CHOICES = [
        (PAYMENT_P, 'Pending'),
        (PAYMENT_C, 'Complete'),
        (PAYMENT_F, 'Failed'),
    ]
    placed_at = models.DateField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICES, default=PAYMENT_P)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, primary_key=True)

    
class Address(models.Model):
    street = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    postal_code = models.IntegerField()
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)





class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=3)

    
    
class Cart(models.Model):
    created_at = models.DateField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
