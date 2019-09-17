from django.forms  import ModelForm
from .models import *

class commetAdd(ModelForm):
     class Meta:
        model = comment
        fields=['article_id','user_name','comments','email','parent']
        
