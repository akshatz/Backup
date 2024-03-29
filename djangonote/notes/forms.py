from django import forms
from .models import Note, Tag


class NoteForm(forms.ModelForm):
	
	class Meta:
		model = Note
		fields = ['label', 'body', 'tags']
		

class TagForm(forms.ModelForm):
	
	class Meta:
		model = Tag
		fields = ['label', ]

