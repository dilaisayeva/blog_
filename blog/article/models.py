from django.db import models
from author.models import author

# Create your models here.
class article(models.Model):
    author_id = models.ForeignKey(author, on_delete=models.CASCADE )
    article_name=models.CharField(max_length=120)
    article_text=models.TextField()

    def __str__(self):
        return self.article_name + ' '+ self.article_text  