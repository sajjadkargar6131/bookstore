from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Book(models.Model) :
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)   
    cover = models.ImageField(upload_to='covers/', blank=True) 

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
   
    
class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    text = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    datetime_created = models.DateTimeField(auto_now_add=True)
    recomended = models.BooleanField(default=True)
    
    def __str__(self) :
        return self.text