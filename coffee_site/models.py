from django.db import models

# Create your models here.

class Customer(models.Model):

    Customer_name = models.CharField(max_length = 250)
    mail = models.CharField(max_length = 250, unique=True)
    phone_number = models.IntegerField(unique=True)


class Menu(models.Model):

        item_name = models.CharField(max_length = 250, unique=True)
        Price = models.IntegerField()


class Order(models.Model):

    menu = models.ForeignKey(Menu, on_delete = models.CASCADE)
    Order_date = models.DateTimeField(blank = True, null=True)
    number_of_items = models.IntegerField(unique=True)
    Bill = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)




class Records(models.Model):

    # Name = models.ForeignKey(Customer, on_delete = models.CASCADE)
    # item_name = models.ForeignKey(Menu, on_delete = models.CASCADE)
    # Bill = models.ForeignKey(Order, on_delete = models.CASCADE)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)


    def publish(self):
        self.published_date = timezone.now()
        self.save()
