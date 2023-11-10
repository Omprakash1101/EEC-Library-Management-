from django.contrib.auth.models import User

from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=225)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural='Categories'
        
    def __str__(self):
        return self.name
    
class Item(models.Model):
    Category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name= models.CharField(max_length=225)     
    
    def __str__(self):
        return self.name
class Books(models.Model):
    Item = models.ForeignKey(Item, related_name='books', on_delete=models.CASCADE)
    name= models.CharField(max_length=225)    
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    