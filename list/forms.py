from .models import TodoModel
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['name','email','work','time']
        labels = {
            'name': 'Enter Your Name',
            'email':'Enter your Email',
            'work':'Work',
            'time':'Time',
        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control',}),
            'email':forms.TextInput(attrs={'class':'form-control',}),
            'work':forms.TextInput(attrs={'class':'form-control',}),
            'time':forms.TimeInput(attrs={'class':'form-control',}),
                  }