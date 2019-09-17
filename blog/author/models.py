from django.db import models




# Create your models here.

class author(models.Model):
    author_name=models.CharField(max_length=30)
    author_surname=models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.author_name + ' '+ self.author_surname

   