from django import forms

from .models import Messages

class MessageValidate(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('broadcasting',)
        
        widgets = {
            'broadcasting': forms.Textarea(attrs={
                'class': 'ml-10 p-6 rounded-lg border '
            })
        }