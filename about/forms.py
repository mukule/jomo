# In forms.py

from django import forms
from .models import About


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['name', 'year_started', 'tag', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Update widget attributes for all fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label,
                'aria-label': field.label,
            })
            field.label = ''
