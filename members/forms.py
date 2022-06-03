from django import forms
from django.forms import formset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from django.forms import ModelForm
from members.models import Individual, Member, EventInfo
from crispy_bootstrap5.bootstrap5 import FloatingField

# then in your Layout
class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ('rider', 'first_name', 'last_name', 'age', 'weight', 'experience', 'comments')
        labels = {
            'rider': 'Rider',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'weight': 'Weight',
            'experience': 'Expertise',
            'comments': 'Comments',
        }
        widget = {
            'rider': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control'}),
            
            'comments': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        self.fields[experience].choices=[("", "BEG", "INT", "ADV", "EXP", "PRO"),] + list(
            self.fields[experience].choices)[1:]
        