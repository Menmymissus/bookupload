from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publication_date=models.DateField(default=None, null=True)
    description=models.TextField()
    image= models.ImageField(upload_to='media')


    def __str__(self):
        return self.title
    
    def delete_book(self):
        self.delete()

    def get_edit_url(self):
        return reverse('edit_book', args=[self.id])   