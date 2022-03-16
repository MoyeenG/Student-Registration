from django import forms

class DetailsForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_deptt = forms.CharField(label='Your Department', max_length=100)
    your_course = forms.CharField(label='Your Course', max_length=100)



