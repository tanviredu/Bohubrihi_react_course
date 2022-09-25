from django.db import models
#
# RELATED_NAME IS FOR REVERSE RELATIONSHIP
#
#
class BookNumber(models.Model):
    isbn_10      = models.CharField(max_length=20,blank=True)
    isbn_13      = models.CharField(max_length=23,blank=True)

    def __str__(self):
        return self.isbn_10

class Book(models.Model):
    title        = models.CharField(max_length=200,blank=False)
    description  = models.CharField(max_length=1000,blank=True)
    price        = models.DecimalField(default=0,max_digits=5,decimal_places=2)
    published    = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    cover        = models.ImageField(upload_to='covers/',blank=True)
    numbers      = models.OneToOneField(BookNumber,null=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Character(models.Model):
    name         = models.CharField(max_length=100)
    book         = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='characters')


    def __str__(self):
        return self.name

class Author(models.Model):
    name         = models.CharField(max_length=30)
    surname      = models.CharField(max_length=30)
    books        = models.ManyToManyField(Book,related_name='authors')

    def __str__(self):
        return str(self.name)