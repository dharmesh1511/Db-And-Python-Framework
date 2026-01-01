from .models import User,Item
from django import forms

class DoctorRegisteration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),

        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']
        