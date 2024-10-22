from django import forms
from .models import Review

class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'title', 'review', 'value']

class CallForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    number = forms.CharField(max_length=23, required=True)
    hour = forms.IntegerField(max_value=23, required=True)
    minute = forms.IntegerField(max_value=59, required=True)
    comment = forms.CharField(max_length=1000, required=True)