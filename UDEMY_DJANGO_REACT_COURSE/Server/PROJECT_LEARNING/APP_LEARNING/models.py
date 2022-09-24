from django.db import models
from django.utils.html import mark_safe
class Book(models.Model):
    title         = models.CharField(max_length=100,unique=True,blank=False)
    descrption    = models.TextField(max_length=256,blank=True)
    price         = models.DecimalField(max_digits=5,decimal_places=2,default=0.0)
    published     = models.DateField(auto_now_add=True,null=True)
    #cover = models.FileField(upload_to="covers/")
    cover         = models.ImageField(upload_to="cover/",blank=True)
    is_published  = models.BooleanField(default=False)
    
    def cover_tag(self):
        return mark_safe('<img src="/media/%s" width="60" height="60" />' % (self.cover))
   

    def __str__(self):
        return self.title
