from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Company'

class About(models.Model):
    image = models.ImageField(upload_to='images', null=True ,blank=True)
    about = models.TextField(null=True, blank=True)
    link=models.TextField(null=True, blank=True)
    def __str__(self):
        return self.about
    
class Statistic(models.Model):
    name = models.CharField(max_length=200)
    count = models.PositiveIntegerField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Statistic'
        verbose_name_plural = 'Statistic'
class Service(models.Model):
    image = models.ImageField(upload_to='img',null=True,blank=True)
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural ='Service'


class Position(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Team(models.Model):
    image = models.ImageField(upload_to='images', null=True, blank=True)
    name = models.CharField(max_length=200)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    telegram = models.CharField(max_length=2000, null=True, blank=True)
    facebook = models.CharField(max_length=2000, null=True, blank=True)
    linkedin = models.CharField(max_length=2000, null=True, blank=True)
    phone = models.CharField(max_length=2000, null=True, blank=True)
    def __str__(self):
        return f"{self.name} | {self.position}"
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'
class Contact(models.Model):
    location = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)

    facebook = models.CharField(max_length=2000)
    instagram = models.CharField(max_length=2000)
    telegram = models.CharField(max_length=2000)
    linkedin = models.CharField(max_length=2000)
    email = models.EmailField(null=True,blank=True)
    def __str__(self):
        return self.address
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'
class Blog(models.Model):
    image = models.ImageField(upload_to='img')
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField()
    viewed = models.IntegerField(default=1)
    def __str__(self):
        return self.name 
    class Meta:
        verbose_name = 'Blog' 
        verbose_name_plural = 'Blog'       
