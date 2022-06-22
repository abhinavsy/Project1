from django.db import models

# Create your models here.
from django.db import models


class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=124)
    phone =models.CharField(max_length=10,null=True)
    email=models.CharField(null=True,blank=False,max_length=30)
    Address_Line=models.CharField(null=True,blank=False,max_length=250)
    Address_Line_2=models.CharField(null=True,blank=False,max_length=250)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name