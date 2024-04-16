from django import forms
from .models import *


class ServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = Service_category
        fields = ['name', 'banner', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Update banner field widget attributes
        self.fields['banner'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Banner',  # Placeholder for banner field
            'title': 'This is the banner for the service category.',  # Help text
        })

        # Set placeholders for all fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'form-control', 'placeholder': field.label})
            field.label = ''


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['category', 'name', 'icon', 'description', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Update icon field widget attributes
        self.fields['icon'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Icon',  # Placeholder for icon field
            'title': 'This is the icon for the service.',  # Help text
        })

        # Set category field as not required
        self.fields['category'].required = False

        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'form-control', 'placeholder': field.label})
            field.label = ''
