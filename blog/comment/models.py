from django.db import models
from article.models import article

# Create your models here.
class comment(models.Model):
    article_id = models.ForeignKey(article, on_delete=models.CASCADE )
    user_name=models.CharField(max_length=120)
    comments=models.TextField()
    email=models.EmailField(max_length=20)
    parent = models.ForeignKey('self',on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user_name + ' '+ self.comments  
