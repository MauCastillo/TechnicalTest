from django.db import models

class PropertyType(models.Model):
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.slug

class State(models.Model):
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.slug

class Category(models.Model):
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.slug
        
class City(models.Model):
    slug = models.SlugField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    zip = models.PositiveIntegerField()

    def __str__(self):
        return self.slug

class Review(models.Model):
    feedback = models.CharField(max_length=128)
    avatar = models.URLField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.feedback

class Transation(models.Model):
    slug = models.SlugField(max_length=50)
    propertyTypes = models.ManyToManyField(PropertyType)
    
    def __str__(self):
        return self.slug


class Property(models.Model):
    title = models.CharField(max_length=128)
    image = models.URLField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sqft = models.PositiveIntegerField()
    baths = models.PositiveIntegerField(default=0)
    beds = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title