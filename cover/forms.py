from urllib.parse import urlencode
from django import forms

class CoverForm(forms.Form):
	title = forms.CharField()
	top_text = forms.CharField()
	author = forms.CharField()

	@property
	def get_params(self):
		if hasattr(self, 'cleaned_data'): #cleaned_data가 있으면
			return urlencode(self.cleaned_data) #출력
		return None #없으면 논