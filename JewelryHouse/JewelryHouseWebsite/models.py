from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=68, blank=False)
    isVerifiedEmail = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return (f'ID: {self.id} | Name: {self.name} | Surname: '
                f'{self.surname} | Email: {self.email} | '
                f'IsVerifiedEmail: {self.isVerifiedEmail}')

class JewelryProduct(models.Model):
    name = models.CharField(max_length=100, blank=False)
    type = models.CharField(max_length=50, blank=False)
    weight = models.FloatField(blank=False)
    price = models.FloatField(blank=False)

    def __str__(self):
        return f'ID: {self.id} | Name: {self.name} | Type: {self.type} | Price: {self.price}'

class Ring(models.Model):
    productID = models.ForeignKey(JewelryProduct, on_delete=models.CASCADE)
    diameter = models.FloatField(blank=False)
    size = models.FloatField(blank=False)
    amount = models.IntegerField(blank=False)
    description = models.CharField(max_length=500, blank = False)

    def __str__(self):
        return (f'ID: {self.id} | ProductID: {self.productID} | Diameter: {self.diameter} | '
                f'Size: {self.size} | Amount: {self.amount}')

class Earring(models.Model):
    productID = models.ForeignKey(JewelryProduct, on_delete=models.CASCADE)
    length = models.FloatField(blank=False)
    width = models.FloatField(blank=False)
    amount = models.IntegerField(blank=False)
    description = models.CharField(max_length=500, blank = False)

    def __str__(self):
        return (f'ID: {self.id} | ProductID: {self.productID} | Length: {self.length} | '
                f'Width: {self.width} | Amount: {self.amount}')

class Necklace(models.Model):
    productID = models.ForeignKey(JewelryProduct, on_delete=models.CASCADE)
    length = models.FloatField(blank=False)
    amount = models.IntegerField(blank=False)
    description = models.CharField(max_length=500, blank = False)

    def __str__(self):
        return (f'ID: {self.id} | ProductID: {self.productID} | Length: {self.length} | '
                f'Amount: {self.amount}')

class Clock(models.Model):
    productID = models.ForeignKey(JewelryProduct, on_delete=models.CASCADE)
    sizeofFace = models.FloatField(blank=False)
    length = models.FloatField(blank=False)
    width = models.FloatField(blank=False)
    amount = models.IntegerField(blank=False)
    description = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return (f'ID: {self.id} | ProductID: {self.productID} | Clock Face Size: {self.sizeofFace} | Length: {self.length} | '
                f'Width: {self.width} | Amount: {self.amount}')
