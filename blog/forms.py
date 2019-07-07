from django import forms
 
 # Create your forms here.

class TagForm(forms.Form):
	title = forms.CharFeild(max_lenght=50)
	slug = forms.CharFeild(max_lenght=50)

	def __init__(self):
		pass