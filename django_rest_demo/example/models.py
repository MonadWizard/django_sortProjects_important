from django.db import models

# Create your models here.

class Industry(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class meta:
        verbose_name_plural = 'Industries'


# একটা company একটা industry তে belong করবে। 
class Company(models.Model):
    name = models.CharField(max_length=200)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class meta:
        verbose_name_plural = 'Companies'



# একটা persion একাধিক company তে কাজ করতে পারে। 
class Person(models.Model):
    name = models.CharField(max_length=200)
    Company = models.ManyToManyField(Company)

    def __str__(self):
        return self.name






