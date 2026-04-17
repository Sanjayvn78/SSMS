from django import forms
from .models import *

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = '__all__'


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = '__all__'

