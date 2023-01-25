from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
class ContactMe(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    content = models.TextField()

    def __str__(self):
        return self.name
    
class Billing(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    address = models.TextField()
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.email

    
