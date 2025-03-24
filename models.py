from django.db import models

# Create your models here.
class Salesperson(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
        return self.last_name

class Invoice(models.Model):
    invoice_number = models.IntegerField()
    date = models.DateField()
    Salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)
    Car = models.ForeignKey(Car, on_delete=models.CASCADE)
    def __str__(self):
        return self.invoice_number

class Car(models.Model):
    serial_number = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.IntegerField()

class Mechanic(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)


class ServiceTicket(models.Model):
    service_number = models.IntegerField()
    Car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_recieved = models.DateField()
    comments = models.TextField()
    date_returned_to_customer = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Service(models.Model):
    service_name = models.CharField(max_length=100)
    hourly_rate = models.IntegerField()

class ServiceMehanic(models.Model):
    ServiceTicket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    Service = models.ForeignKey(Service, on_delete=models.CASCADE)
    Mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    hours = models.IntegerField()
    comments = models.TextField()
    rate = models.IntegerField()

class Parts(models.Model):
    parts_number = models.IntegerField()
    description = models.TextField()
    purchase_price = models.IntegerField()
    retail_price = models.IntegerField()






