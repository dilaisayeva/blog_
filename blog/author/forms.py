from django.forms  import ModelForm
from .models import *

class authorAdd(ModelForm):
     class Meta:
        model = author
        fields=['author_name','author_surname']
        
