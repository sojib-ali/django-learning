from django.db import models

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    


class Collection(models.Model):
    title = models.CharField(max_length=50)
    featured_product = models.ForeignKey('Product', on_delete= models.SET_NULL, null= True, related_name = "+")

    def __str__(self):
        return self.title
    
    class Meta: 
        ordering = ['title']



class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, related_name = 'prod_collections')
    promotions = models.ManyToManyField(Promotion, related_name = "products")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']





class Customer(models.Model):
    class Membership(models.TextChoices):
        Bronze = 'B', 'Bronze'
        Silver = 'S', 'Silver'
        Gold = 'G', 'Gold'

    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    email = models.EmailField( max_length=100, unique=True)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=Membership, default=Membership.Bronze)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['first_name', 'last_name']




class Order(models.Model):
    class Payment_status(models.TextChoices):
        Pending = 'p', 'Pending'
        Complete = 'C', 'Complete'
        Failed = 'F', 'Failed'
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=Payment_status, default=Payment_status.Pending)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='orderitems')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)



class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE, primary_key=True)
    


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    


