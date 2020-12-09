import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffee_lover.settings')



import django

django.setup()


import random
from coffee_site.models import Customer, Menu, Order, Records
from faker import Faker

fakegen=Faker()

def call(N=10):
    num = 1
    for i in range(N):

        cust_name = fakegen.name()
        cust_mail = fakegen.email()
        numb1 = fakegen.random_number(digits=10)
        date = fakegen.date()
        numb2 = fakegen.random_number(digits=1)
        menu = Menu
        customer = Customer.objects.get_or_create(Customer_name = cust_name, mail = cust_mail, phone_number = numb1)[0]
        #menu = Menu.objects.get_or_create(Price = price)[0]
        #order = Order.objects.get_or_create(item_name = Menu, Order_date = date, number_of_items = numb2)[0]



        num = num+1




# customers = ['Raju','Krishna','Bimol','Kancha','Bapon','Prakash']
#
# def add_customer():
#     c = Customer.objects.get_or_create(customer_name=random.choice(customers))[0]
#     c.save()
#     return c
#
#
# def populate(N=10):
#
#     for entry in range(N):
#         customer_name = customer_name()
#
#
#         fake_email = fakegen.email()
#         fake_phone_number = fakegen.phone_number()
#         fake_item_name = fakegen.item_name()
#         fake_Order_date = fakegen.Order_date()
#         fake_number_of_items = fakegen.number_of_items()
#         fake_Bill = fakegen.Bill()
#         fake_price = fakegen.Price()
#
#
#
#         menu = Menu.objects.get_or_create(item_name = fake_item_name, Price = fake_price)[0]
#
#         order = Order.objects.get_or_create(item_name = fake_item_name, Order_date = fake_Order_date, number_of_items = fake_number_of_items, Bill = fake_Bill, Customer_name = customer_name, menu = menu, customer = c)[0]
#
#         records = Records.objects.get_or_create(Bill = fake_Bill, item_name = fake_item_name, Customer_name = customer_name, phone_number = fake_phone_number, order = order, customer = c)[0]


if __name__ == '__main__':
    print('Populating script..')
    call(10)
    print('Populating complete!')
