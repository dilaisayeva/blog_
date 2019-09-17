from django.forms  import ModelForm
from .models import *

class articleAdd(ModelForm):
     class Meta:
        model = article
        fields=['article_name','article_text','author_id']
        
