from django import forms 

class LoginForm(forms.Form):

	user_name = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.TextInput())

