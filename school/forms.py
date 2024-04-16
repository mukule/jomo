from django import forms
from .models import *


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'tag', 'description', 'logo', 'banner']

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


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'tag', 'description',
                  'flyer', 'price']  # Include 'price' field

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label,
            })
            field.label = ''
