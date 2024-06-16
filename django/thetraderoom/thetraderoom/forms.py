from django import forms
class usersForm(forms.Form):
    num1=forms.CharField(label="Value 1:",required=False)
    num2=forms.CharField(label="Value 2:",required=False)
    num3=forms.CharField(label="Value 3:",required=False)
    email=forms.EmailField