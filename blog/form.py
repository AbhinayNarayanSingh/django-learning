from django import forms


# class FeedbackForm(forms.Form):
#     name=forms.CharField(max_length=250)
#     email=forms.EmailField(max_length=254)
#     subject=forms.CharField(max_length=250)
#     message=forms.CharField(widget=forms.Textarea)


from django.forms import ModelForm
from .models import *

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        # fields = '__all__'
        fields = ['name', 'email','subject','message']