from django import forms
from .models import Service_category


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
