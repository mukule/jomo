from django import forms
from .models import *


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'banner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label,
            })
            field.label = ''


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Make the category field not editable
        self.fields['category'].widget.attrs['disabled'] = True
        self.fields['category'].required = False

        # Update widget attributes for other fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',  # Add 'form-control' class
                'placeholder': field.label,  # Use field label as placeholder
                'label': ''  # Set empty label
            })
