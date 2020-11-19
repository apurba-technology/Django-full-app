from django import forms  
from .models import *

class BannerForm(forms.ModelForm): 
  
    class Meta: 
        model = Banner 
        fields = ['name', 'banner_image'] 


class admin_regestion_meForm(forms.ModelForm):
	class Meta:
		model=admin_regestion_me
		fields="__all__"