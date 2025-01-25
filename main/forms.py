from django import forms
from .models import DemoForm

class DemoFormForm(forms.ModelForm):
    class Meta:
        model = DemoForm
        fields = ['name', 'email', 'phone', 'message']
        labels = {
        'message': 'Interested Course (Elaborate if you want to specify your demand.)',
        }
        widgets = {
            'message': forms.Textarea(attrs={
                'style': 'width:100%;',
                'rows': 4,  # Optional: Specifies the height of the textarea
            }),
        }
