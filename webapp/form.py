from django import forms
from .models import Feedback, Join

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['email']

class JoinForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = ['name', 'address', 'email']


