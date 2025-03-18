
from .models import Item
from django import forms
STYLE_TAIL_CLASSES = 'w-full p-4 rounded-lg border'

class NewListing(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('listing_name',  'listing_price', 'listing_description', 'listing_image','listing_category')
        widgets = {
            'listing_name': forms.TextInput(attrs={
                'class': STYLE_TAIL_CLASSES
            }),
            'listing_price': forms.TextInput(attrs={
                'class': STYLE_TAIL_CLASSES
            }),
             'listing_description': forms.Textarea(attrs={
                'class': STYLE_TAIL_CLASSES
            }),
             'listing_image': forms.FileInput(attrs={
                'class': STYLE_TAIL_CLASSES
            }),
            'listing_category': forms.Select(attrs={
                'class': STYLE_TAIL_CLASSES
            }),
            
           
        }

# class EditItemForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         fields = ('name', 'description', 'price', 'image', 'is_sold')
#         widgets = {
#             'name': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'description': forms.Textarea(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'price': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'image': forms.FileInput(attrs={
#                 'class': INPUT_CLASSES
#             })
#         }